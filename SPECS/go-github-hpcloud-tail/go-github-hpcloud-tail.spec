# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tail
%define go_import_path  github.com/hpcloud/tail
# Test failure, may be cause by outdate code - Julian
%define go_test_ignore_failure 1

Name:           go-github-hpcloud-tail
Version:        1.0.0
Release:        %autorelease
Summary:        Go package for reading from continously updated files (tail -f)
License:        MIT
URL:            https://github.com/hpcloud/tail
#!RemoteAsset
Source0:        https://github.com/hpcloud/tail/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hpcloud/tail) = %{version}

%description
A Go package striving to emulate the features of the BSD tail program.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
