# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assume-no-moving-gc
%define go_import_path  go4.org/unsafe/assume-no-moving-gc
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id b99613f794b6b2f6d80da53bb131c5c98ea2fdd2

Name:           go-go4-unsafe-assume-no-moving-gc
Version:        0+git20260108.b99613f
Release:        %autorelease
Summary:        Package to declare Go code that play unsafe GC games
License:        BSD-3-Clause
URL:            https://github.com/go4org/unsafe-assume-no-moving-gc
#!RemoteAsset
Source0:        https://github.com/go4org/unsafe-assume-no-moving-gc/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(go4.org/unsafe/assume-no-moving-gc) = %{version}

%description
go4.org/unsafe/assume-no-moving-gc

If your Go package wants to declare that it plays unsafe games that only
work if the Go runtime's garbage collector is not a moving collector,
then add:

  import _ "go4.org/unsafe/assume-no-moving-gc"

Then your program will explode if that's no longer the case. (Users can
override the explosion with a scary sounding environment variable.)

This also gives us a way to find all the really gross unsafe packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
