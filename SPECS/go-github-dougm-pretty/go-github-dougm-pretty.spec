# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pretty
%define go_import_path  github.com/dougm/pretty
%define package_version 2011-12-22
# It's a fork, and the test have not compitable with upstream - Julian
%define go_test_ignore_failure 1

Name:           go-github-dougm-pretty
Version:        2011.12.22
Release:        %autorelease
Summary:        Pretty printing for Go values
License:        MIT
URL:            https://github.com/dougm/pretty
#!RemoteAsset
Source0:        https://github.com/dougm/pretty/archive/refs/tags/go.weekly.%{package_version}.tar.gz#/%{_name}-%{package_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dougm/pretty) = %{version}

%description
Package pretty provides pretty-printing for Go values.

%files
%doc Readme*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
