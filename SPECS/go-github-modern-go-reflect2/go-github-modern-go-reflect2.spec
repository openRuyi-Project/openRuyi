# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           reflect2
%define go_import_path  github.com/modern-go/reflect2

Name:           go-github-modern-go-reflect2
Version:        1.0.2
Release:        %autorelease
Summary:        reflect api without runtime reflect.Value cost
License:        Apache-2.0
URL:            https://github.com/modern-go/reflect2
#!RemoteAsset
Source0:        https://github.com/modern-go/reflect2/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/modern-go/reflect2) = %{version}

%description
This package provides reflect api that avoids runtime reflect.Value cost

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
