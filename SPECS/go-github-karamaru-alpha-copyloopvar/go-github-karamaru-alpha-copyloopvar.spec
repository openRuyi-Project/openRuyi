# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           copyloopvar
%define go_import_path  github.com/karamaru-alpha/copyloopvar

Name:           go-github-karamaru-alpha-copyloopvar
Version:        1.2.2
Release:        %autorelease
Summary:        Copyloopvar is a linter detects places where loop variables are copied
License:        MIT
URL:            https://github.com/karamaru-alpha/copyloopvar
#!RemoteAsset:  sha256:b759029172b7599ad9092278cc6b506ada773f150ba8b2062f5fb134f83472b4
Source0:        https://github.com/karamaru-alpha/copyloopvar/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/karamaru-alpha/copyloopvar) = %{version}

Requires:       go(golang.org/x/tools)

%description
Copyloopvar is a linter detects places where loop variables are copied.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n copyloopvar-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/karamaru-alpha/copyloopvar

%changelog
%autochangelog
