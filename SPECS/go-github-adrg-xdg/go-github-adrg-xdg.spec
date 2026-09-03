# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xdg
%define go_import_path  github.com/adrg/xdg

Name:           go-github-adrg-xdg
Version:        0.5.3
Release:        %autorelease
Summary:        Go implementation of the XDG Base Directory Specification and XDG user directories
License:        MIT
URL:            https://github.com/adrg/xdg
#!RemoteAsset:  sha256:ba6b5b287a6e8f5ba5c03768d3f55bc69f60b18050ec17c867fb20c060add28b
Source0:        https://github.com/adrg/xdg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/adrg/xdg) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Go implementation of the XDG Base Directory Specification, XDG User
Directories and XDG Icon Theme specifications, with cross-platform support
for locating configuration, data, cache and runtime files.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
