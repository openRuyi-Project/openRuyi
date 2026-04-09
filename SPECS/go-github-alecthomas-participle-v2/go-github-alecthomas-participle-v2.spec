# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           participle
%define go_import_path  github.com/alecthomas/participle
%define go_test_exclude github.com/alecthomas/participle/lexer/internal/conformance

Name:           go-github-alecthomas-participle-v2
Version:        2.1.4
Release:        %autorelease
Summary:        A parser library for Go
License:        MIT
URL:            https://github.com/alecthomas/participle
#!RemoteAsset
Source0:        https://github.com/alecthomas/participle/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

Provides:       go(github.com/alecthomas/participle/v2) = %{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/assert)
BuildRequires:  go(github.com/alecthomas/kong)
BuildRequires:  go(github.com/alecthomas/repr)

%description
A dead simple parser package for Go

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
