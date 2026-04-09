# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           argv
%define go_import_path  github.com/cosiner/argv

Name:           go-github-cosiner-argv
Version:        0.1.0
Release:        %autorelease
Summary:        A library for Go to split command line string into arguments array.
License:        MIT
URL:            https://github.com/cosiner/argv
#!RemoteAsset
Source0:        https://github.com/cosiner/argv/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cosiner/argv) = %{version}

%description
Argv is a  library for Go to split command line
string into arguments array.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
