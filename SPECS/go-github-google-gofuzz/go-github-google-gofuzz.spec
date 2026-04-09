# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gofuzz
%define go_import_path  github.com/google/gofuzz

Name:           go-github-google-gofuzz
Version:        1.2.0
Release:        %autorelease
Summary:        Fuzz testing for go.
License:        Apache-2.0
URL:            https://github.com/google/gofuzz
#!RemoteAsset
Source0:        https://github.com/google/gofuzz/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/gofuzz) = %{version}

%description
gofuzz is a library for populating go objects with random values.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
