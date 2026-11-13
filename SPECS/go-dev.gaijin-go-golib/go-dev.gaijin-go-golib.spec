# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golib
%define go_import_path  dev.gaijin.team/go/golib

Name:           go-dev.gaijin-go-golib
Version:        0.8.1
Release:        %autorelease
Summary:        Shared Go utilities from Gaijin Entertainment
License:        MIT
URL:            https://github.com/GaijinEntertainment/golib
#!RemoteAsset:  sha256:1c9e477efedbfa16d0cb1799f207f15ba5e3dcbaca6730873393434139200a6b
Source0:        https://github.com/GaijinEntertainment/golib/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n golib-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(dev.gaijin.team/go/golib) = %{version}
Provides:       go(dev.gaijin.team/go/golib/build) = %{version}
Provides:       go(dev.gaijin.team/go/golib/e) = %{version}
Provides:       go(dev.gaijin.team/go/golib/fields) = %{version}
Provides:       go(dev.gaijin.team/go/golib/http/sign) = %{version}
Provides:       go(dev.gaijin.team/go/golib/logger) = %{version}
Provides:       go(dev.gaijin.team/go/golib/logger/bufferadapter) = %{version}
Provides:       go(dev.gaijin.team/go/golib/logger/logrusadapter) = %{version}
Provides:       go(dev.gaijin.team/go/golib/logger/slogadapter) = %{version}
Provides:       go(dev.gaijin.team/go/golib/logger/zapadapter) = %{version}
Provides:       go(dev.gaijin.team/go/golib/must) = %{version}
Provides:       go(dev.gaijin.team/go/golib/stacktrace) = %{version}
Provides:       go(dev.gaijin.team/go/golib/testing/freeport) = %{version}

Requires:       go(github.com/sirupsen/logrus)
Requires:       go(go.uber.org/zap)

%description
Shared Go utilities from Gaijin Entertainment.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
