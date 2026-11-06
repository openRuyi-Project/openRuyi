# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wastedassign
%define go_import_path  github.com/sanposhiho/wastedassign/v2

Name:           go-github-sanposhiho-wastedassign
Version:        2.1.0
Release:        %autorelease
Summary:        Wastedassign finds wasted assignment statements
License:        MIT
URL:            https://github.com/sanposhiho/wastedassign
#!RemoteAsset:  sha256:7621f9ddf73ab3aa14e47095602e04172fd65691673bf39dbfd0a9035c5ae306
Source0:        https://github.com/sanposhiho/wastedassign/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Downstream: diagnostic text is data, not a printf format string.
Patch2000:      2000-format-diagnostic-reasons-as-data.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/sanposhiho/wastedassign/v2) = %{version}

Requires:       go(golang.org/x/tools)

%description
Wastedassign finds wasted assignment statements.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n wastedassign-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/sanposhiho/wastedassign/v2

%changelog
%autochangelog
