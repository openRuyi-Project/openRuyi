# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mergo
%define go_import_path  github.com/imdario/mergo

Name:           go-github-imdario-mergo
Version:        0.3.10
Release:        %autorelease
Summary:        Merge Go structs and maps
License:        BSD-3-Clause
URL:            https://github.com/imdario/mergo
#!RemoteAsset:  sha256:4c198781290376dccbc957179d9d8d6a0a15b81647e1ddcb8b8856294bfc3e3d
Source0:        https://github.com/imdario/mergo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Legacy tests pass dynamic strings to testing.Errorf.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/imdario/mergo) = %{version}

%description
Merge Go structs and maps.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
