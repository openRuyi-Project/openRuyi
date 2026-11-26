# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fileutil
%define go_import_path  modernc.org/fileutil

Name:           go-modernc-fileutil
Version:        1.4.0
Release:        %autorelease
Summary:        Package fileutil collects some file utility functions
License:        BSD-3-Clause
URL:            https://gitlab.com/cznic/fileutil
#!RemoteAsset:  git+https://gitlab.com/cznic/fileutil.git#2543588afcb295e9914df64339955f24ccc2d811
#!CreateArchive
Source0:        %{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(modernc.org/mathutil)

Provides:       go(modernc.org/fileutil) = %{version}

Requires:       go(modernc.org/mathutil)

%description
Package fileutil collects some file utility functions.

%files
%doc README
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
