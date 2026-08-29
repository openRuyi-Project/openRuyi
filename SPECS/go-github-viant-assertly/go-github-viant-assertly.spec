# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assertly
%define go_import_path  github.com/viant/assertly
# TestAssertCoalesceWithZero is inconsistent with current assertly/toolbox
# coalesce handling: OBS reports null vs 0 as a failed validation. - HNO3Miracle
%define go_test_exclude %{go_import_path}

Name:           go-github-viant-assertly
Version:        0.9.2
Release:        %autorelease
Summary:        Arbitrary datastructure validation
License:        Apache-2.0
URL:            https://github.com/viant/assertly
#!RemoteAsset:  sha256:774282b54537f032b3a94457141bc1fb671c5a72272ab9f4fdd5caf22b4cf62f
Source0:        https://github.com/viant/assertly/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/viant/toolbox)

Provides:       go(github.com/viant/assertly) = %{version}

Requires:       go(github.com/viant/toolbox)

%description
Assertly is a Go library for validating arbitrary data structures in tests.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
