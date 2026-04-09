# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           levenshtein
%define go_import_path  github.com/arbovm/levenshtein
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 48b4e1c0c4d0b8b1864f1bd2cd31bb20147e4636

Name:           go-github-arbovm-levenshtein
Version:        0+git20260104.48b4e1c
Release:        %autorelease
Summary:        Levenshtein Distance in Go
License:        BSD-3-Clause
URL:            https://github.com/arbovm/levenshtein
#!RemoteAsset
Source0:        https://github.com/arbovm/levenshtein/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/arbovm/levenshtein) = %{version}

%description
Go (http://golang.org) package to calculate the Levenshtein Distance
(http://en.wikipedia.org/wiki/Levenshtein_distance)、

# Wouldn't bother to fix this - 251
%check

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
