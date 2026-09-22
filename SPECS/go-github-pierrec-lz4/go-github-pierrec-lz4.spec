# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lz4
%define go_import_path  github.com/pierrec/lz4
%define go_test_include  %{go_import_path}

Name:           go-github-pierrec-lz4
Version:        2.0.5
Release:        %autorelease
Summary:        LZ4 compression library for Go
License:        BSD-3-Clause
URL:            https://github.com/pierrec/lz4
VCS:            git:https://github.com/pierrec/lz4.git
#!RemoteAsset:  sha256:322b98493c960e940cf187646957bea4fe96a274412b88d7d199a9cbf39591c6
Source0:        https://github.com/pierrec/lz4/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n lz4-2.0.5

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pierrec/lz4) = %{version}

%description
This package provides the github.com/pierrec/lz4 Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
