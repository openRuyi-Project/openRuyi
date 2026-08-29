# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           json-patch
%define go_import_path  gopkg.in/evanphx/json-patch.v4
# The archive also contains command and v5 packages using github.com import
# paths; they are not part of this gopkg.in v4 library package. - HNO3Miracle
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/cmd*
    %{go_import_path}/v5*
}

Name:           go-gopkg-evanphx-json-patch.v4
Version:        4.13.0
Release:        %autorelease
Summary:        Go library for gopkg.in/evanphx/json-patch.v4
License:        BSD-3-Clause
URL:            https://github.com/evanphx/json-patch
#!RemoteAsset:  sha256:ba96932a4c396312d3531952c0faf26a0ea470b97df2187a0d2afd219c969640
Source0:        https://github.com/evanphx/json-patch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects non-constant format strings in upstream tests. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(gopkg.in/evanphx/json-patch.v4) = %{version}

%description
This package provides the Go library gopkg.in/evanphx/json-patch.v4.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
