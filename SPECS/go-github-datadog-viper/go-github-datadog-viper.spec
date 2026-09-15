# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           viper
%define go_import_path  github.com/DataDog/viper

Name:           go-github-datadog-viper
Version:        1.15.3
Release:        %autorelease
Summary:        DataDog configuration library for Go applications
License:        MIT
URL:            https://github.com/DataDog/viper
#!RemoteAsset:  sha256:eaaa31c149cbd33bfccd3a53182dc5d0ee55cc844d6e91a7c964bd7b198a2751
Source0:        https://github.com/DataDog/viper/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep overflow detection stable with the packaged newer spf13/cast.
Patch2000:      2000-detect-size-overflow-without-cast-behavior.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/BurntSushi/toml)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/jwalterweatherman)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/magiconair/properties)
Requires:       go(github.com/pelletier/go-toml)
Requires:       go(github.com/spf13/cast)
Requires:       go(github.com/spf13/jwalterweatherman)
Requires:       go(github.com/spf13/pflag)
Requires:       go(go.yaml.in/yaml/v2)

%description
This DataDog-maintained Viper fork provides configuration files, environment
variables, flags, and remote configuration support for Go applications.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
