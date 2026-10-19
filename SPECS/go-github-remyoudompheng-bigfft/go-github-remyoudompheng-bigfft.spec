# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bigfft
%define go_import_path  github.com/remyoudompheng/bigfft
%define commit_id       24d4a6f8daece64d3c9a7660d4ee0974c4e31021

Name:           go-github-remyoudompheng-bigfft
Version:        0+git20230129.24d4a6f
Release:        %autorelease
Summary:        Schonhage-Strassen method for multiplying integers
License:        BSD-3-Clause
URL:            https://github.com/remyoudompheng/bigfft
#!RemoteAsset:  sha256:473cc0d422fb44d375d2d8c229e32a498130e1e4867ae730bd2e965938d26edb
Source0:        https://github.com/remyoudompheng/bigfft/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/remyoudompheng/bigfft) = %{version}

%description
This library is a toy proof-of-concept implementation of the well-known
Schonhage-Strassen method for multiplying integers. It is not expected to have
a real life usecase outside number theory computations, nor is it expected to
be used in any production system.

%files
%doc README
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
