# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hm
%define go_import_path  github.com/chewxy/hm

Name:           go-github-chewxy-hm
Version:        1.0.0
Release:        %autorelease
Summary:        a simple Hindley-Milner type system in Go
License:        MIT
URL:            https://github.com/chewxy/hm
#!RemoteAsset
Source0:        https://github.com/chewxy/hm/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/xtgo/set)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/chewxy/hm) = %{version}

Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/xtgo/set)
Requires:       go(github.com/stretchr/testify)

%description
Package hm is a simple Hindley-Milner type inference system in Go. It
provides the necessary data structures and functions for creating such a
system.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
