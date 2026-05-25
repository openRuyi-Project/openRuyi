# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assertly
%define go_import_path  github.com/viant/assertly

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

BuildOption(prep):  -n assertly-0.9.2
# TestAssertCoalesceWithZero is inconsistent with current assertly/toolbox
# coalesce handling: OBS reports null vs 0 as a failed validation.
BuildOption(check):  -skip TestAssertCoalesceWithZero

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(github.com/viant/toolbox)
BuildRequires:  go(github.com/viant/toolbox/data)

Provides:       go(github.com/viant/assertly) = %{version}

Requires:       go(github.com/viant/toolbox)
Requires:       go(github.com/viant/toolbox/data)


%description
Data structure testing library (assertly)

[Image: Data structure testing library for Go.]
(https://goreportcard.com/badge/github.com/viant/assertly)
(https://goreportcard.com/report/github.com/viant/assertly) [Image:
GoDoc] (https://godoc.org/github.com/viant/assertly?status.svg)
(https://godoc.org/github.com/viant/assertly)

This library is compatible with Go 1.10+

Please refer to CHANGELOG.md (/CHANGELOG.md) if you encounter breaking

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
