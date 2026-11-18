# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-exhaustruct
%define go_import_path  dev.gaijin.team/go/exhaustruct/v4

Name:           go-dev.gaijin-go-exhaustruct-v4
Version:        4.0.0
Release:        %autorelease
Summary:        Go analyzer for exhaustive struct initialization
License:        MIT
URL:            https://github.com/GaijinEntertainment/go-exhaustruct
#!RemoteAsset:  sha256:82f9bc57223d6ef1c7c9eac22437189d51df21ac3a811c8a88fbb6b0d7c1e261
Source0:        https://github.com/GaijinEntertainment/go-exhaustruct/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Load the fixture package explicitly with current go/packages.
Patch2000:      2000-load-structure-test-package.patch

BuildOption(prep):  -n go-exhaustruct-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(dev.gaijin.team/go/golib)
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(dev.gaijin.team/go/exhaustruct/v4) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v4/analyzer) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v4/cmd/exhaustruct) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v4/internal/comment) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v4/internal/pattern) = %{version}
Provides:       go(dev.gaijin.team/go/exhaustruct/v4/internal/structure) = %{version}

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
