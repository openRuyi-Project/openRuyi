# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           memory
%define go_import_path  modernc.org/memory

Name:           go-modernc-memory
Version:        1.11.0
Release:        %autorelease
Summary:        Package memory implements a memory allocator
License:        BSD-3-Clause
URL:            https://gitlab.com/cznic/memory
#!RemoteAsset:  git+https://gitlab.com/cznic/memory.git#0a6f7544739330ad95572cc272626a60176f2faf
#!CreateArchive
Source0:        %{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(modernc.org/mathutil)

Provides:       go(modernc.org/memory) = %{version}

Requires:       go(golang.org/x/sys)

%description
Package memory implements a memory allocator.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
