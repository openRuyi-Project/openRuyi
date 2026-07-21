# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name            scaleway-sdk-go
%define go_import_path   github.com/scaleway/scaleway-sdk-go
%define upstream_version 1.0.0-beta.36

Name:           go-github-scaleway-scaleway-sdk-go
Version:        1.0.0~beta36
Release:        %autorelease
Summary:        Scaleway API SDK for Go
License:        Apache-2.0
URL:            https://github.com/scaleway/scaleway-sdk-go
#!RemoteAsset:  sha256:8045f3664c48e7b1c4fee92bc4d78d120a5619a1ef002b6b909a5b8b335c8216
Source0:        https://github.com/scaleway/scaleway-sdk-go/archive/v%{upstream_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{upstream_version}
# Current Go vet rejects a non-constant Debugf format string in scw tests.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/dnaeon/go-vcr.v4)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/scaleway/scaleway-sdk-go) = %{version}

Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/dnaeon/go-vcr.v4)
Requires:       go(gopkg.in/yaml.v2)

%description
This package provides the Scaleway API SDK for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
