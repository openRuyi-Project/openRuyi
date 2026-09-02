# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fx
%define go_import_path  go.uber.org/fx

Name:           go-uber-fx
Version:        1.24.0
Release:        %autorelease
Summary:        Dependency injection framework for Go applications
License:        MIT
URL:            https://github.com/uber-go/fx
#!RemoteAsset:  sha256:f9dd56167c1eb3d365d5b10ea83564789ea582c25136d08b3a01edbc89d7cd5c
Source0:        https://github.com/uber-go/fx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Documentation server tests share port 8080 and must run sequentially.
BuildOption(check):  -p 1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/dig)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(go.uber.org/dig)
Requires:       go(go.uber.org/multierr)
Requires:       go(go.uber.org/zap)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)

%description
Fx is a dependency injection framework for assembling Go applications from
reusable, composable modules.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
