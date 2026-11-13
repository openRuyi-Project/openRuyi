# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-exhaustruct
%define go_import_path  dev.gaijin.team/go/exhaustruct/v5

Name:           go-dev.gaijin-go-exhaustruct-v5
Version:        5.2.0
Release:        %autorelease
Summary:        Go analyzer for exhaustive struct initialization
License:        MIT
URL:            https://github.com/GaijinEntertainment/go-exhaustruct
#!RemoteAsset:  sha256:70548828be4075c0d18e794dc9220d232fba4a414bc00cb29440d7fbc1e08500
Source0:        https://github.com/GaijinEntertainment/go-exhaustruct/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-exhaustruct-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(dev.gaijin.team/go/golib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(dev.gaijin.team/go/exhaustruct/v5) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v5/analyzer) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v5/cmd/exhaustruct) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v5/internal/astutil) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v5/internal/cache) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v5/internal/directive) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v5/internal/pattern) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v5/internal/structure) = %{version}

Requires:       go(dev.gaijin.team/go/golib)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for exhaustive struct initialization.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
