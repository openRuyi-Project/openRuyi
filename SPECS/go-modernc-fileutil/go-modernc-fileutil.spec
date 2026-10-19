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
#!RemoteAsset:  sha256:a5c4b0d98f8cf4b8c4594cc9158dfa9752ef9486419571610f72481e72fb0cd6
Source0:        https://gitlab.com/cznic/fileutil/-/archive/v%{version}/fileutil-v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
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
