# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           musttag
%define go_import_path  go-simpler.org/musttag

Name:           go-go-simpler-musttag
Version:        0.14.0
Release:        %autorelease
Summary:        Go analyzer for required struct tags
License:        MPL-2.0
URL:            https://github.com/go-simpler/musttag
#!RemoteAsset:  sha256:6210533e63779f8658d3744eebaf6bfbed56b20d01f0b6d08d09fbc62bdae215
Source0:        https://github.com/go-simpler/musttag/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n musttag-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/jmoiron/sqlx)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(go-simpler.org/assert)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(go-simpler.org/musttag) = %{version}
Provides:       go(go-simpler.org/musttag/cmd/musttag) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for required struct tags.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
