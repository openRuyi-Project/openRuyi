# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           set
%define go_import_path  github.com/fatih/set

Name:           go-github-fatih-set
Version:        0.2.1
Release:        %autorelease
Summary:        Provides both threadsafe and non-threadsafe implementations of a generic set data structure
License:        MIT
URL:            https://github.com/fatih/set
#!RemoteAsset:  sha256:8b1d0bf1529083f9c29cf82e5c8419d8705797c4470a41ec74cf4d4dd373622f
Source0:        https://github.com/fatih/set/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/fatih/set) = %{version}

%description
Set is a basic and simple, hash-based, **Set** data structure
implementation in Go (Golang).

Set provides both threadsafe and non-threadsafe implementations of a
generic set data structure. The thread safety encompasses all operations
on one set. Operations on multiple sets are consistent in that the
elements of each set used was valid at exactly one point in time between
the start and the end of the operation. Because it's thread safe, you
can use it concurrently with your goroutines.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
