# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jet
%define go_import_path  github.com/CloudyKit/jet

Name:           go-github-cloudykit-jet
Version:        6.3.1
Release:        %autorelease
Summary:        Jet Template Engine for Go
License:        Apache-2.0
URL:            https://github.com/cloudykit/jet
#!RemoteAsset
Source0:        https://github.com/cloudykit/jet/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/CloudyKit/fastprinter)

Provides:       go(github.com/CloudyKit/jet) = %{version}

%description
Jet is a template engine developed to be easy to use, powerful, dynamic,
yet secure and very fast.

 * simple and familiar syntax
 * supports template inheritance (extends) and composition (block/yield,
   import, include)
 * descriptive error messages with filename and line number
 * auto-escaping
 * simple C-like expressions
 * very fast execution – Jet can execute templates faster than some pre-
   compiled template engines
 * very light in terms of allocations and memory footprint

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
