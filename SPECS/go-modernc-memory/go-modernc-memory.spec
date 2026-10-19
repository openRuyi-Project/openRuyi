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
#!RemoteAsset:  sha256:d9b141d67ab64feafc90be428419ee048af852fbac4f33164dcf5e5d15c41272
Source0:        https://gitlab.com/cznic/memory/-/archive/v%{version}/memory-v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
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
