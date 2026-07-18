# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xz
%define go_import_path  github.com/ulikunitz/xz

Name:           go-github-ulikunitz-xz
Version:        0.5.15
Release:        %autorelease
Summary:        Pure golang package for reading and writing xz-compressed files
License:        BSD-2-Clause
URL:            https://github.com/ulikunitz/xz
#!RemoteAsset:  sha256:d75d8560d25ac1d9729769e084134e047565ea9f5f908175eddb4372a7687505
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/ulikunitz/xz) = %{version}

%description
This Go language package supports the reading and writing of xz compressed streams.
It includes also a gxz command for compressing and decompressing data. The package
is completely written in Go and doesn't have any dependency on any C code.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
