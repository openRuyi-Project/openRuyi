# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gocheckcompilerdirectives
%define go_import_path  4d63.com/gocheckcompilerdirectives

Name:           go-4d63-gocheckcompilerdirectives
Version:        1.4.0
Release:        %autorelease
Summary:        Go analyzer for compiler directive comments
License:        MIT
URL:            https://github.com/leighmcculloch/gocheckcompilerdirectives
#!RemoteAsset:  sha256:c0f3924167b9c1e641460c560849768384a973442daa7de7d77dfa86ecfe6e59
Source0:        https://github.com/leighmcculloch/gocheckcompilerdirectives/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gocheckcompilerdirectives-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(4d63.com/gocheckcompilerdirectives) = %{version}
Provides:       go(4d63.com/gocheckcompilerdirectives/checkcompilerdirectives) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for compiler directive comments.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
