# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rardecode
%define go_import_path  github.com/nwaples/rardecode/v2

Name:           go-github-nwaples-rardecode-v2
Version:        2.4.1
Release:        %autorelease
Summary:        A go package for reading RAR archives
License:        BSD-2-Clause
URL:            https://github.com/nwaples/rardecode
#!RemoteAsset:  sha256:0955f47559c2b5a657536dda8cecfcef2c1775b38b06477da41e8b7352b4cb5a
Source0:        https://github.com/nwaples/rardecode/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/nwaples/rardecode/v2) = %{version}

%description
A go package for reading RAR archives.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
