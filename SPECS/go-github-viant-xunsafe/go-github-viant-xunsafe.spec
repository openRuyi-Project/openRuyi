# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xunsafe
%define go_import_path  github.com/viant/xunsafe

Name:           go-github-viant-xunsafe
Version:        0.11.0
Release:        %autorelease
Summary:        Faster golang reflection
License:        Apache-2.0
URL:            https://github.com/viant/xunsafe
#!RemoteAsset:  sha256:6469d8d733b0f3665490c1db48b4eee03a1dfb7cf6c7f3bcccee32333651adf0
Source0:        https://github.com/viant/xunsafe/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n xunsafe-0.11.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/stretchr/testify/assert)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/viant/xunsafe) = %{version}
Provides:       go(github.com/viant/xunsafe/converter) = %{version}


%description
xunsafe (faster golang reflection)

[Image: GoReportCard]
(https://goreportcard.com/badge/github.com/viant/xunsafe)
(https://goreportcard.com/report/github.com/viant/xunsafe) [Image:
GoDoc] (https://godoc.org/github.com/viant/xunsafe?status.svg)
(https://godoc.org/github.com/viant/xunsafe)

This library is compatible with Go 1.17+

Please refer to CHANGELOG.md (/CHANGELOG.md) if you encounter breaking

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
