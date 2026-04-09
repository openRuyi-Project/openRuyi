# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           murmur3
%define go_import_path  github.com/spaolacci/murmur3

Name:           go-github-spaolacci-murmur3
Version:        1.0.0
Release:        %autorelease
Summary:        Native MurmurHash3 Go implementation
License:        BSD-3-Clause
URL:            https://github.com/spaolacci/murmur3
#!RemoteAsset
Source0:        https://github.com/spaolacci/murmur3/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/spaolacci/murmur3) = %{version}

%description
Native Go implementation of Austin Appleby's third MurmurHash revision
(aka MurmurHash3).

Reference algorithm has been slightly hacked as to support the streaming
mode required by Go's standard Hash interface
(http://golang.org/pkg/hash/#Hash).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
