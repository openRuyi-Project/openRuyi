# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           viper
%define go_import_path  github.com/spf13/viper
%global go_test_exclude github.com/spf13/viper/remote

Name:           go-github-spf13-viper
Version:        1.21.0
Release:        %autorelease
Summary:        Go configuration with fangs
License:        MIT
URL:            https://github.com/spf13/viper
#!RemoteAsset
Source0:        https://github.com/spf13/viper/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-viper/mapstructure/v2)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/sagikazarmark/locafero)
BuildRequires:  go(github.com/spf13/afero)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/subosito/gotenv)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/spf13/viper) = %{version}

Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-viper/mapstructure/v2)
Requires:       go(github.com/pelletier/go-toml/v2)
Requires:       go(github.com/sagikazarmark/locafero)
Requires:       go(github.com/spf13/afero)
Requires:       go(github.com/spf13/cast)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/subosito/gotenv)
Requires:       go(go.yaml.in/yaml/v3)

%description
Viper is a complete configuration solution for Go applications including
12-Factor apps (https://12factor.net/#the_twelve_factors). It is
designed
to work within any application, and can handle all types of
configuration needs and formats. It supports:

 * setting defaults
 * setting explicit values
 * reading config files
 * dynamic discovery of config files across multiple locations
 * reading from environment variables
 * reading from remote systems (e.g. Etcd or Consul)
 * reading from command line flags
 * reading from buffers
 * live watching and updating configuration
 * aliasing configuration keys for easy refactoring

Viper can be thought of as a registry for all of your applications'
configuration needs.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
