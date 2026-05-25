# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           freetype
%define go_import_path  github.com/golang/freetype
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id  e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4

Name:           go-github-golang-freetype
Version:        0+git20260106.e2365df
Release:        %autorelease
Summary:        The Freetype font rasterizer in the Go programming language
License:        FTL OR GPL-2.0-or-later
URL:            https://github.com/golang/freetype
#!RemoteAsset:  sha256:00ce141869e009f102f51fb8f9c2a611decb67083e4c1de7842bc9eafad8676b
Source0:        https://github.com/golang/freetype/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go vet reports a non-constant fmt.Fprint call in a generated-data test.
# - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)

Provides:       go(github.com/golang/freetype) = %{version}

Requires:       go(golang.org/x/image)

%description
The Freetype font rasterizer in the Go programming language.

Freetype-Go is derived from Freetype, which is written in C. Freetype is
copyright 1996-2010 David Turner, Robert Wilhelm, and Werner Lemberg.
Freetype-Go is copyright The Freetype-Go Authors, who are listed in the
AUTHORS file.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
