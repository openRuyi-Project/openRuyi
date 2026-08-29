# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           selinux
%define go_import_path  github.com/opencontainers/selinux

Name:           go-github-opencontainers-selinux
Version:        1.11.0
Release:        %autorelease
Summary:        Common SELinux implementation for Go
License:        Apache-2.0
URL:            https://github.com/opencontainers/selinux
#!RemoteAsset:  sha256:d8fd24e3882e0a5d70ab81c2b6560dbc105294da04c93fec9fc172e098b67e8d
Source0:        https://github.com/opencontainers/selinux/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/opencontainers/selinux) = %{version}

Requires:       go(golang.org/x/sys)

%description
selinux provides common SELinux helpers for Go container software.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
