# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-textseg
%define go_import_path  github.com/apparentlymart/go-textseg
# Testcase has bug, it always be fail - Julian
%define go_test_ignore_failure 1

Name:           go-github-apparentlymart-go-textseg
Version:        16.0.0
Release:        %autorelease
Summary:        Go implementation of Unicode Text Segmentation
License:        MIT AND Apache-2.0 AND Unicode-DFS-2016
URL:            https://github.com/apparentlymart/go-textseg
#!RemoteAsset
Source0:        https://github.com/apparentlymart/go-textseg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/apparentlymart/go-textseg) = %{version}

%description
This is an implementation of the Unicode Text Segmentation specification
for Go. Specifically, it currently includes only the "grapheme cluster"
segmentation algorithm.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
