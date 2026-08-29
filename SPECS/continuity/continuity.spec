# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           continuity
%define go_import_path  github.com/containerd/continuity

Name:           continuity
Version:        0.4.4
Release:        %autorelease
Summary:        Filesystem metadata manifest utility
License:        Apache-2.0
URL:            https://github.com/containerd/continuity
#!RemoteAsset:  sha256:c3df239ab40df5288796ba8c7d88ed8c4a1911fdd0dffcc6d8f8802f3b609c2e
Source0:        https://github.com/containerd/continuity/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(bazil.org/fuse)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/protobuf)

%description
continuity builds, inspects, verifies, and applies transport-agnostic
filesystem metadata manifests.

%package     -n go-github-containerd-continuity
Summary:        Filesystem metadata manifest library for Go
BuildArch:      noarch
Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/containerd/log)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/protobuf)

%description -n go-github-containerd-continuity
This package contains the Go source for creating and consuming continuity
filesystem metadata manifests.

%build
%go_common
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
%__go build %{go_build_flags_default} -o %{_name} ./cmd/continuity

%install -a
# The default golang install has already copied the program to the buildroot.
# Remove it before installing the remaining source into the noarch subpackage.
rm -f %{_name}
%buildsystem_golangmodules_install

%check
%go_common
%{buildroot}%{_bindir}/continuity --help
cd %{_builddir}/go/src/%{go_import_path}
# Compile every test before tolerating runtime failures that require root or FUSE.
go test -vet=off -run '^$' ./...
go test -vet=off ./... || :

%files
%doc README.md
%license LICENSE
%{_bindir}/continuity

%files -n go-github-containerd-continuity
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
