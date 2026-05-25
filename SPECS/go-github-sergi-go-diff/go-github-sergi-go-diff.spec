# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-diff
%define go_import_path  github.com/sergi/go-diff

Name:           go-github-sergi-go-diff
Version:        1.4.0
Release:        %autorelease
Summary:        Diff Match Patch library for Go
License:        MIT
URL:            https://github.com/sergi/go-diff
#!RemoteAsset:  sha256:22b94323762b49f1f6985dfce0bc5ec8f43b3a5ddaceb1b577c00038d25c8d3d
Source0:        https://github.com/sergi/go-diff/archive/refs/tags/v1.4.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-diff-1.4.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/sergi/go-diff) = %{version}
Provides:       go(github.com/sergi/go-diff/diffmatchpatch) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/stretchr/testify)
Requires:       go(gopkg.in/check.v1)
Requires:       go(gopkg.in/yaml.v2)

%description
This package provides Diff Match Patch library for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
