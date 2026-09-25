# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           koanf
%define go_import_path  github.com/knadh/koanf
%define go_test_include %{go_import_path}

Name:           go-github-knadh-koanf
Version:        1.5.0
Release:        %autorelease
Summary:        Extensible configuration management library for Go
License:        MIT
URL:            https://github.com/knadh/koanf
#!RemoteAsset:  sha256:e451f971636d67fbc5dbf84850f2ea5d20cda3bf24646e727b60bed878c5f28a
Source0:        https://github.com/knadh/koanf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/fatih/structs)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/hashicorp/consul/api)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/hashicorp/vault/api)
BuildRequires:  go(github.com/hjson/hjson-go/v4)
BuildRequires:  go(github.com/joho/godotenv)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/npillmayer/nestext)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/rhnvrm/simples3)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/knadh/koanf/maps)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/mitchellh/mapstructure)

%description
Koanf reads configuration from multiple sources and formats through a
lightweight, extensible Go API.

%install
install -d %{buildroot}%{go_sys_gopath}/%{go_import_path}
install -p -m 0644 *.go go.mod go.sum \
    %{buildroot}%{go_sys_gopath}/%{go_import_path}/

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}/*.go
%{go_sys_gopath}/%{go_import_path}/go.mod
%{go_sys_gopath}/%{go_import_path}/go.sum

%changelog
%autochangelog
