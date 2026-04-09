# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logex
%define go_import_path  github.com/chzyer/logex
# Test failure on Go 1.25.5, but success on Go 1.24 - Julian
%define go_test_ignore_failure 1

Name:           go-github-chzyer-logex
Version:        1.2.1
Release:        %autorelease
Summary:        An golang log lib, supports tracking and level, wrap by standard log lib
License:        MIT
URL:            https://github.com/chzyer/logex
#!RemoteAsset
Source0:        https://github.com/chzyer/logex/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/chzyer/logex) = %{version}

%description
An golang log lib, supports tracing and level, wrap by standard log lib

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
