# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           docker-cli
%define go_import_path  github.com/docker/cli
%define docker_commit   4a63305d74332de5ceba7fcbccbc3cbb7412f5ba

Name:           docker-cli
Version:        29.8.1
Release:        %autorelease
Summary:        Docker command-line client
License:        Apache-2.0
URL:            https://github.com/docker/cli
#!RemoteAsset:  sha256:55bcae5053f0914118d229658e2ac3a877dbdead6cb2c322e525d0c1e8bf78d2
Source0:        https://github.com/docker/cli/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# The docker/cli release archive extracts to a cli-<version> directory.
BuildOption(prep):  -n cli-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go-md2man
BuildRequires:  git

Provides:       docker = %{version}-%{release}
Requires:       moby

%description
The Docker CLI is the command-line client for the Docker daemon. It provides
the docker command used to build, run and manage containers, images, networks
and volumes.

%build
# docker/cli has no root main package for %build from the golang buildsystem.
# Upstream encapsulated the actual `go build` into `scripts/build/binary`,
# which builds ./cmd/docker with version ldflags and tags into build/docker.
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
export VERSION=%{version}
export GITCOMMIT=%{docker_commit}
export GOTOOLCHAIN=local
export GO_LINKMODE=dynamic
./scripts/build/binary
# Upstream has no go.mod; its helper temporarily links vendor.mod as go.mod.
GO111MODULE=on GO_MD2MAN=%{_bindir}/go-md2man \
    ./scripts/with-go-mod.sh ./scripts/docs/generate-man.sh
./scripts/build/shell-completion

%install
cd %{_builddir}/go/src/%{go_import_path}
install -D -m 0755 build/docker %{buildroot}%{_bindir}/docker
install -d %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man5
install -p -m 0644 man/man1/*.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 man/man5/*.5 %{buildroot}%{_mandir}/man5/
install -D -m 0644 build/completion/bash/docker %{buildroot}%{bash_completions_dir}/docker
install -D -m 0644 build/completion/zsh/_docker %{buildroot}%{zsh_completions_dir}/_docker
install -D -m 0644 build/completion/fish/docker.fish %{buildroot}%{fish_completions_dir}/docker.fish

%check
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
# Several golden-file tests format timestamps and expect UTC.
export TZ=UTC
# e2e requires a live Docker daemon; cmd/docker-trust is a nested module.
pkgs=$(%{__go} list ./... 2>/dev/null | grep -vE '/e2e(/|$)|/cmd/docker-trust(/|$)')
%{__go} test %{go_test_flags_default} -vet=off -short \
    -skip 'TestRunBuildFromGitHubSpecialCase|TestConnectAndWait' $pkgs

%files
%doc README.md
%license LICENSE NOTICE
%{_bindir}/docker
%{_mandir}/man1/docker*.1*
%{_mandir}/man5/docker-config-json.5*
%{_mandir}/man5/Dockerfile.5*
%{bash_completions_dir}/docker
%{zsh_completions_dir}/_docker
%{fish_completions_dir}/docker.fish

%changelog
%autochangelog
