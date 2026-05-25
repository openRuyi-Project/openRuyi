# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name             yaml
%define go_import_path    go.yaml.in/yaml/v4
%define upstream_version  4.0.0-rc.4

Name:           go-go.yaml-yaml-v4
Version:        4.0.0~rc4
Release:        %autorelease
Summary:        YAML support for the Go language
License:        Apache-2.0
URL:            https://github.com/yaml/go-yaml
#!RemoteAsset:  sha256:f3ae68f40578781cd6fe0f86f6967dcc08bd012f57e8be1738f1f9e36f1dcfdb
Source0:        https://github.com/yaml/go-yaml/archive/v%{upstream_version}.tar.gz#/%{_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-yaml-%{upstream_version}
# The yts package requires external YAML Test Suite data files:
# "Run 'make test-data' to download them first". Offline OBS builds cannot
# download test data during %check, so keep the rest of the repository tested.
%define go_test_exclude go.yaml.in/yaml/v4/yts

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
