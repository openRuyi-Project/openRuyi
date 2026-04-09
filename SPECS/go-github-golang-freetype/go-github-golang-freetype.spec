# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           freetype
%define go_import_path  github.com/golang/freetype
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id  e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4

Name:           go-github-golang-freetype
Version:        0+git20260106.e2365df
Release:        %autorelease
Summary:        The Freetype font rasterizer in the Go programming language.
License:        FTL OR GPL-2.0-or-later
URL:            https://github.com/golang/freetype
#!RemoteAsset
Source0:        https://github.com/golang/freetype/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}
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
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
