# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           color
%define go_import_path  github.com/gookit/color

Name:           go-github-gookit-color
Version:        1.6.1
Release:        %autorelease
Summary:        A command-line color library with 16/256/True color support, universal API methods and Windows support.
License:        MIT
URL:            https://github.com/gookit/color
#!RemoteAsset:  sha256:52f4ed971bf10563c590a01a6601db11b064d069cfe2120562ecae13fc7120c8
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/xo/terminfo)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(github.com/gookit/assert)

Provides:       go(github.com/gookit/color) = %{version}

Requires:       go(github.com/xo/terminfo)
Requires:       go(golang.org/x/sys)
Requires:       go(github.com/gookit/assert)

%description
Terminal color rendering library, support 8/16 colors,
256 colors, RGB color rendering output, support
Print/Sprintf methods, compatible with Windows.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
