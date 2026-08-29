# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           zip
%define go_import_path  github.com/STARRY-S/zip

Name:           go-github-starry-s-zip
Version:        0.2.3
Release:        %autorelease
Summary:        Provides support for reading and writing ZIP archives
License:        BSD-3-Clause
URL:            https://github.com/STARRY-S/zip
#!RemoteAsset:  sha256:19f5e969ad85e13262843096fc511e7d0653133659f20a1835500a884641179b
Source0:        https://github.com/STARRY-S/zip/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/STARRY-S/zip) = %{version}

%description
Go zip library

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
