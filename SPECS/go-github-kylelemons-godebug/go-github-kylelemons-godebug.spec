# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           godebug
%define go_import_path  github.com/kylelemons/godebug

Name:           go-github-kylelemons-godebug
Version:        1.1.0
Release:        %autorelease
Summary:        Debugging helper utilities for Go
License:        Apache-2.0
URL:            https://github.com/kylelemons/godebug
#!RemoteAsset
Source0:        https://github.com/kylelemons/godebug/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kylelemons/godebug) = %{version}

%description
Pretty Printing for Go

Have you ever wanted to get a pretty-printed version of a Go data
structure, complete with indentation?  I have found this especially
useful in unit tests and in debugging my code, and thus godebug was
born!

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
