# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vsock
%define go_import_path  github.com/mdlayher/vsock

Name:           go-github-mdlayher-vsock
Version:        1.2.1
Release:        %autorelease
Summary:        Package vsock provides access to Linux VM sockets (AF_VSOCK) for communication between a hypervisor and its virtual machines.  MIT Licensed.
License:        MIT
URL:            https://github.com/mdlayher/vsock
#!RemoteAsset:  sha256:0abaf26f54abec90f6387c2ab0824d9ede750b920231aef60820175bb4b843ac
Source0:        https://github.com/mdlayher/vsock/archive/refs/tags/v1.2.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n vsock-1.2.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/net/nettest)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/errgroup)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)

Provides:       go(github.com/mdlayher/vsock) = %{version}
Provides:       go(github.com/mdlayher/vsock/internal/vsutil) = %{version}

Requires:       go(github.com/mdlayher/socket)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/unix)


%description
vsock [Image: Test Status]
(https://github.com/mdlayher/vsock/workflows/Linux%20Test/badge.svg)
(https://github.com/mdlayher/vsock/actions) [Image: Go Reference]
(https://pkg.go.dev/badge/github.com/mdlayher/vsock.svg)
(https://pkg.go.dev/github.com/mdlayher/vsock)  [Image: Go Report Card]
(https://goreportcard.com/badge/github.com/mdlayher/vsock)
(https://goreportcard.com/report/github.com/mdlayher/vsock)

Package vsock provides access to Linux VM sockets (AF_VSOCK) for
communication between a hypervisor and its virtual machines.  MIT
Licensed.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
