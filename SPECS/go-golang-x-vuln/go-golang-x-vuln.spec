# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vuln
%define go_import_path  golang.org/x/vuln

# Preserve binary-analysis fixtures as data, including their original symbols.
%define __brp_strip     %{nil}
%define _binaries_in_noarch_packages_terminate_build  0
%define __provides_exclude_from  ^%{go_sys_gopath}/golang.org/x/vuln/.*testdata/.*$
%define __requires_exclude_from  ^%{go_sys_gopath}/golang.org/x/vuln/.*testdata/.*$

Name:           go-golang-x-vuln
Version:        1.9.0
Release:        %autorelease
Summary:        Go vulnerability detection and analysis libraries
License:        BSD-3-Clause
URL:            https://github.com/golang/vuln
#!RemoteAsset:  sha256:e5a0151c6516d7485750058984280fcf9332c4693f968164192fe92f454a04bb
Source0:        https://github.com/golang/vuln/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n vuln-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmdtest)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/renameio)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/telemetry)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/expect)
BuildRequires:  go(golang.org/x/tools/go/packages/packagestest)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(golang.org/x/vuln) = %{version}
Provides:       go(golang.org/x/vuln/cmd/govulncheck) = %{version}
Provides:       go(golang.org/x/vuln/cmd/govulncheck/integration/internal/integration) = %{version}
Provides:       go(golang.org/x/vuln/cmd/govulncheck/integration/k8s) = %{version}
Provides:       go(golang.org/x/vuln/cmd/govulncheck/integration/stackrox-scanner) = %{version}
Provides:       go(golang.org/x/vuln/internal) = %{version}
Provides:       go(golang.org/x/vuln/internal/buildinfo) = %{version}
Provides:       go(golang.org/x/vuln/internal/client) = %{version}
Provides:       go(golang.org/x/vuln/internal/derrors) = %{version}
Provides:       go(golang.org/x/vuln/internal/gosym) = %{version}
Provides:       go(golang.org/x/vuln/internal/goversion) = %{version}
Provides:       go(golang.org/x/vuln/internal/govulncheck) = %{version}
Provides:       go(golang.org/x/vuln/internal/openvex) = %{version}
Provides:       go(golang.org/x/vuln/internal/osv) = %{version}
Provides:       go(golang.org/x/vuln/internal/sarif) = %{version}
Provides:       go(golang.org/x/vuln/internal/scan) = %{version}
Provides:       go(golang.org/x/vuln/internal/semver) = %{version}
Provides:       go(golang.org/x/vuln/internal/test) = %{version}
Provides:       go(golang.org/x/vuln/internal/testenv) = %{version}
Provides:       go(golang.org/x/vuln/internal/traces) = %{version}
Provides:       go(golang.org/x/vuln/internal/vulncheck) = %{version}
Provides:       go(golang.org/x/vuln/internal/web) = %{version}
Provides:       go(golang.org/x/vuln/scan) = %{version}

Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/telemetry)
Requires:       go(golang.org/x/tools)

%description
Go vulnerability detection and analysis libraries.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
