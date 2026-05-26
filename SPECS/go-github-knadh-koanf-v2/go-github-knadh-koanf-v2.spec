# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           koanf
%define go_import_path  github.com/knadh/koanf/v2
# The repository also contains examples, parsers, and optional providers that
# require external backend modules such as AWS, Azure, Consul, Vault, and etcd.
# This package provides the core koanf/v2 module, so keep %check scoped to it. - HNO3Miracle
%define go_test_include %{go_import_path}

Name:           go-github-knadh-koanf-v2
Version:        2.3.4
Release:        %autorelease
Summary:        Lightweight extensible configuration management library for Go
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:6d0673028357e83bb9ac1b54329763a8acdc13a717f69416f4859dce81f4e184
Source0:        https://github.com/knadh/koanf/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/knadh/koanf/maps)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/reflectwalk)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/knadh/koanf/v2) = %{version}

Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/knadh/koanf/maps)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/reflectwalk)

%description
Koanf is a library for reading configuration from multiple sources and
providing it through a consistent Go API.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
