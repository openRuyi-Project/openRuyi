# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wrapcheck
%define go_import_path  github.com/tomarrell/wrapcheck/v2

Name:           go-github-tomarrell-wrapcheck
Version:        2.13.0
Release:        %autorelease
Summary:        A simple Go linter to check that errors from external packages are wrapped
License:        MIT
URL:            https://github.com/tomarrell/wrapcheck
#!RemoteAsset:  sha256:a15c24556a88c8ead2e2a796019853d482b0e5d741fb09660a6d6e9d47e01295
Source0:        https://github.com/tomarrell/wrapcheck/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/gobwas/glob)
BuildRequires:  go(github.com/hashicorp/hcl)
BuildRequires:  go(github.com/magiconair/properties)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/jwalterweatherman)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/subosito/gotenv)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/ini.v1)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/tomarrell/wrapcheck/v2) = %{version}
Provides:       go(github.com/tomarrell/wrapcheck/v2/wrapcheck) = %{version}

Requires:       go(github.com/gobwas/glob)
Requires:       go(github.com/spf13/viper)
Requires:       go(golang.org/x/tools)

%description
A simple Go linter to check that errors from external packages are wrapped.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n wrapcheck-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/tomarrell/wrapcheck/v2

%changelog
%autochangelog
