# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gojsonschema
%define go_import_path  github.com/xeipuuv/gojsonschema

Name:           go-github-xeipuuv-gojsonschema
Version:        1.2.0
Release:        %autorelease
Summary:        Go library packaged for syft dependency resolution
License:        Apache-2.0
URL:            https://github.com/xeipuuv/gojsonschema
#!RemoteAsset:  sha256:ad47429e26a7078df155bffe2d3ff2e967fb0d6be185b5ffe995d6731916bcf7
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Reject comma-separated fractional seconds for RFC3339 time formats - Jvle
Patch2000:      2000-reject-comma-time-fractions.patch

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/xeipuuv/gojsonreference)

Provides:       go(github.com/xeipuuv/gojsonschema) = %{version}

Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/xeipuuv/gojsonreference)

%description
Go library packaged for syft dependency resolution.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
