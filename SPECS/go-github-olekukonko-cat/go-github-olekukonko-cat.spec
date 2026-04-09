# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cat
%define go_import_path  github.com/olekukonko/cat
# Upstream does not provide git tags, use commit ID instead - 251
%define commit_id 50322a0618f6f48488d955217745beecac3a3d5c

Name:           go-github-olekukonko-cat
Version:        0+git20260107.50322a0
Release:        %autorelease
Summary:        cat - Because life's too short for ugly string building code.
License:        MIT
URL:            https://github.com/olekukonko/cat
#!RemoteAsset
Source0:        https://github.com/olekukonko/cat/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/olekukonko/cat) = %{version}

%description
The Fast & Fluent String Concatenation Library for Go

Go's strings.Builder is great, but building complex strings often feels
clunky. cat makes string concatenation:

 * **Faster** - Optimized paths for common types, zero-allocation
   conversions
 * **Fluent** - Chainable methods for beautiful, readable code
 * **Flexible** - Handles any type, nested structures, and custom
   formatting
 * **Smart** - Automatic pooling, size estimation, and separator
   handling

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
