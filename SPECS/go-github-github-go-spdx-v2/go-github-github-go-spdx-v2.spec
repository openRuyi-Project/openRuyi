# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-spdx
%define go_import_path  github.com/github/go-spdx/v2

Name:           go-github-github-go-spdx-v2
Version:        2.7.0
Release:        %autorelease
Summary:        Golang implementation of a checker for determining if an SPDX ID satisfies an SPDX Expression
License:        MIT
URL:            https://github.com/github/go-spdx
#!RemoteAsset:  sha256:a6954d98e4c6e6f6e416c771037caac7a61affdc3f4203c32870700816db793f
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/github/go-spdx/v2) = %{version}

Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/stretchr/testify)

%description
Golang implementation of a checker for determining
if a set of SPDX IDs satisfies an SPDX Expression.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
