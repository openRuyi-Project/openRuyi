# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ciinfo
%define go_import_path  github.com/gkampitakis/ciinfo
# compile-constants is a generated helper directory and fails as a standalone
# package in %check: FAIL github.com/gkampitakis/ciinfo/compile-constants [build failed].
# - HNO3Miracle
%define go_test_exclude github.com/gkampitakis/ciinfo/compile-constants

Name:           go-github-gkampitakis-ciinfo
Version:        0.3.4
Release:        %autorelease
Summary:        CI environment detection library for Go
License:        MIT
URL:            https://github.com/gkampitakis/ciinfo
#!RemoteAsset:  sha256:01ff7e99659ded6fe512aec1282129456847837bfd31e609db9be2508b312beb
Source0:        https://github.com/gkampitakis/ciinfo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gkampitakis/ciinfo) = %{version}

%description
ciinfo detects CI environments for Go projects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
