# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fs
%define go_import_path  github.com/kr/fs

Name:           go-github-kr-fs
Version:        0.1.0
Release:        %autorelease
Summary:        Package fs provides filesystem-related functions.
License:        BSD-3-Clause
URL:            https://github.com/kr/fs
#!RemoteAsset
Source0:        https://github.com/kr/fs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kr/fs) = %{version}

%description
Filesystem Package

http://godoc.org/github.com/kr/fs

%files
%license LICENSE*
%doc Readme*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
