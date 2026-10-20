# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           spinner
%define go_import_path  github.com/briandowns/spinner

Name:           go-github-briandowns-spinner
Version:        1.23.2
Release:        %autorelease
Summary:        Terminal spinner and progress indicators
License:        Apache-2.0
URL:            https://github.com/briandowns/spinner
#!RemoteAsset:  sha256:7741d8b38aa70606627b51c5957bb00ae4a90726fbf8fcddb42d413373782c5e
Source0:        https://github.com/briandowns/spinner/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(golang.org/x/term)

Provides:       go(github.com/briandowns/spinner) = %{version}

Requires:       go(github.com/fatih/color)
Requires:       go(golang.org/x/term)

%description
Spinner provides configurable terminal progress indicators, including character
sets, colors, animation speed, and output writers.

%prep -a
# Use distribution packages instead of the upstream vendor tree in both copies.
rm -rf vendor %{_builddir}/go/src/%{go_import_path}/vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
