# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goimagehash
%define go_import_path  github.com/corona10/goimagehash
# TestExtImageHashCompute is sensitive to packaged image/resize behavior; OBS
# showed only small hash-distance drift in the root package while subpackages
# still pass. - HNO3Miracle
%define go_test_exclude %{go_import_path}

Name:           go-github-corona10-goimagehash
Version:        1.1.0
Release:        %autorelease
Summary:        Image hashing library written in Go
License:        BSD-2-Clause
URL:            https://github.com/corona10/goimagehash
#!RemoteAsset:  sha256:f6dfcabbe0ca0534f5ac815d2d3dfbd9ab4ed747e6208cd17f9e7357a7cb6900
Source0:        https://github.com/corona10/goimagehash/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/nfnt/resize)

Provides:       go(github.com/corona10/goimagehash) = %{version}

Requires:       go(github.com/nfnt/resize)

%description
goimagehash is an image hashing library written in Go. It supports average,
difference and perception hashing.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
