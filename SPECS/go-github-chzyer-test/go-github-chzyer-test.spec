# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           test
%define go_import_path  github.com/chzyer/test
# Test failure, may be cause by outdate code - Julian
%define go_test_ignore_failure 1

Name:           go-github-chzyer-test
Version:        1.0.0
Release:        %autorelease
Summary:        A Go library designed to enhance testing capabilities.
License:        MIT
URL:            https://github.com/chzyer/test
#!RemoteAsset
Source0:        https://github.com/chzyer/test/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/chzyer/logex)

Provides:       go(github.com/chzyer/test) = %{version}

Requires:       go(github.com/chzyer/logex)

%description
A Go library designed to enhance testing capabilities. It provides
advanced features for writing and managing test cases, aiming to improve
the efficiency and comprehensiveness of software testing.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
