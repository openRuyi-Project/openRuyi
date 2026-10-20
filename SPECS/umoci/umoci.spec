# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name umoci
%global go_import_path github.com/opencontainers/umoci

Name:           umoci
Version:        0.6.0
Release:        %autorelease
Summary:        umoci modifies Open Container images
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://umo.ci/
VCS:            git:https://github.com/opencontainers/umoci
#!RemoteAsset:  sha256:8fca9947afe42c86468be9eb87e74269cb7ae2c292c2008212bd197c4c88aeec
Source0:        https://github.com/opencontainers/umoci/releases/download/v%{version}/umoci.tar.xz
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go-md2man
BuildRequires:  go(github.com/apex/log)
BuildRequires:  go(github.com/blang/semver/v4)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/pgzip)
BuildRequires:  go(github.com/moby/sys)
BuildRequires:  go(github.com/mohae/deepcopy)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/rootless-containers/proto)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/urfave/cli)
BuildRequires:  go(github.com/vbatts/go-mtree)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf/proto)

%description
umoci is a reference implementation of the OCI image specification and
provides users with the ability to create, manipulate, and otherwise
interact with container images. It is designed to be as small and
unopinionated as possible, so as to act as a foundation for larger
systems to be built on top of.

%prep -a
# The golang prep stage has copied the source into its GOPATH workspace.
# Remove both vendor trees so every dependency comes from distribution packages.
rm -rf vendor %{_builddir}/go/src/%{go_import_path}/vendor
rm -f doc/man/.gitignore doc/site/.gitignore

# The golang build system builds '.', but the root package is a library.
# Build the CLI entry point explicitly and generate its manual pages.
%build
%go_common
cd %{_builddir}/go/src/%{go_import_path}
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%__go build %{go_build_flags_default} -o %{_builddir}/%{_name} ./cmd/umoci
for manpage in doc/man/*.md; do
    go-md2man -in "${manpage}" -out "${manpage%.md}"
done

%install
install -D -m 0755 %{_builddir}/%{_name} %{buildroot}%{_bindir}/%{_name}
install -d %{buildroot}%{_mandir}/man1
cp -p %{_builddir}/go/src/%{go_import_path}/doc/man/*.1 %{buildroot}%{_mandir}/man1/

%files
%doc CHANGELOG.md CONTRIBUTING.md GOVERNANCE.md README.md RELEASES.md doc
%license COPYING
%{_bindir}/umoci
%{_mandir}/man1/umoci*

%changelog
%autochangelog
