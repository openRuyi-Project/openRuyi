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
Summary:        Linux VM socket support for Go
License:        MIT
URL:            https://github.com/mdlayher/vsock
#!RemoteAsset:  sha256:0abaf26f54abec90f6387c2ab0824d9ede750b920231aef60820175bb4b843ac
Source0:        https://github.com/mdlayher/vsock/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/mdlayher/vsock) = %{version}

Requires:       go(github.com/mdlayher/socket)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)

%description
Package vsock provides access to Linux VM sockets (AF_VSOCK) for communication
between a hypervisor and its virtual machines.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
