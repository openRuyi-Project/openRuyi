# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           envy
%define go_import_path  github.com/gobuffalo/envy

Name:           go-github-gobuffalo-envy
Version:        1.7.1
Release:        %autorelease
Summary:        Package envy makes working with ENV variables in Go trivial
License:        MIT
URL:            https://github.com/gobuffalo/envy
VCS:            git:https://github.com/gobuffalo/envy.git
#!RemoteAsset:  sha256:f7745c63da532e0c6b920e0657a09b3295b7da8bb2b7a3870c0f2c50da611d0b
Source0:        https://github.com/gobuffalo/envy/archive/v1.7.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n envy-1.7.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/joho/godotenv)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/gobuffalo/envy) = %{version}

Requires:       go(github.com/joho/godotenv)
Requires:       go(github.com/rogpeppe/go-internal)

%description
This package provides the github.com/gobuffalo/envy Go module source.

%files
%doc README.md
%license LICENSE
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
