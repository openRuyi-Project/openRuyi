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

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/viant/xunsafe) = %{version}

%description
This package provides unsafe-based helpers for faster reflection-style field
access in Go.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%license NOTICE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
