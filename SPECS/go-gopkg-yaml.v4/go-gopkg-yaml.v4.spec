# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name             yaml
%define go_import_path    go.yaml.in/yaml/v4
%define upstream_version  4.0.0-rc.6
# The yts package requires external YAML Test Suite data files:
# "Run 'make test-data' to download them first". Offline OBS builds cannot
# download test data during %check, so keep the rest of the repository tested - HNO3Miracle
%define go_test_exclude go.yaml.in/yaml/v4/yts

Name:           go-gopkg-yaml.v4
Version:        4.0.0~rc6
Release:        %autorelease
Summary:        YAML support for the Go language
License:        Apache-2.0
URL:            https://github.com/yaml/go-yaml
#!RemoteAsset:  sha256:7c580dfcca58ab33af4235913ff106b25de50dead4d73f0fd375b77db79ddb82
Source0:        https://github.com/yaml/go-yaml/archive/v%{upstream_version}.tar.gz#/%{_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go vet rejects %q for libyaml Kind and Style in upstream node tests; keep
# tests enabled but disable vet. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(go.yaml.in/yaml/v4) = %{version}

%description
This package provides YAML encoding and decoding support for Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
