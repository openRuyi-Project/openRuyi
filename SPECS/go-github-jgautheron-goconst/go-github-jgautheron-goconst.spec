# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goconst
%define go_import_path  github.com/jgautheron/goconst

Name:           go-github-jgautheron-goconst
Version:        1.11.0
Release:        %autorelease
Summary:        Finds repeated strings that could be replaced by a constant
License:        MIT
URL:            https://github.com/jgautheron/goconst
#!RemoteAsset:  sha256:ec92d99b8ca697b9ba650baf4a7856bbe52af8cd65f71eb42b939761bdb994bc
Source0:        https://github.com/jgautheron/goconst/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/jgautheron/goconst) = %{version}

%description
Finds repeated strings that could be replaced by a constant.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n goconst-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/jgautheron/goconst

%changelog
%autochangelog
