# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           socket
%define go_import_path  github.com/mdlayher/socket

Name:           go-github-mdlayher-socket
Version:        0.6.0
Release:        %autorelease
Summary:        Low-level network connection helpers for Go
License:        MIT
URL:            https://github.com/mdlayher/socket
#!RemoteAsset:  sha256:4832cc911767d0a22f3b7c4288518d51c522ed43ee0b3128554952c1b9016c6e
Source0:        https://github.com/mdlayher/socket/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/mdlayher/socket) = %{version}

Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)

%description
Package socket provides low-level network connection types that integrate with
Go's runtime network poller for asynchronous I/O and deadline support.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
