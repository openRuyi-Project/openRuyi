# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lzip-go
%define go_import_path  github.com/sorairolake/lzip-go

Name:           go-github-sorairolake-lzip-go
Version:        0.3.8
Release:        %autorelease
Summary:        Implements the lzip compressed format
License:        Apache-2.0 AND MIT
URL:            https://github.com/sorairolake/lzip-go
#!RemoteAsset:  sha256:92aba643fa24e56c868e451e0b8e1297100ad1ba7ca4dfab7bfaff0cf8025d09
Source0:        https://github.com/sorairolake/lzip-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmdtest)
BuildRequires:  go(github.com/ulikunitz/xz)

Provides:       go(github.com/sorairolake/lzip-go) = %{version}

Requires:       go(github.com/google/go-cmdtest)
Requires:       go(github.com/ulikunitz/xz)

%description
This package supports reading and writing of lzip compressed streams.

%files
%doc README.md
%license LICENSE-APACHE
%license LICENSE-MIT
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
