# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golibs
%define go_import_path  github.com/AdguardTeam/golibs
# Exclude otelutil (needs otel/semconv/v1.34.0 not packaged in openRuyi) and sentry subpackages (unused and unpackaged).
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/otelutil*
    %{go_import_path}/sentryutil*
    %{go_import_path}/testutil/sentrytest*
}

Name:           go-github-adguardteam-golibs
Version:        0.35.20
Release:        %autorelease
Summary:        Go utility packages primarily used in AdGuard projects
License:        Unlicense
URL:            https://github.com/AdguardTeam/golibs
#!RemoteAsset:  sha256:a7144e6d635585e5a727fc0a3840e0b38df97e321a7178812fdef382b863f41e
Source0:        https://github.com/AdguardTeam/golibs/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/c2h5oh/datasize)
BuildRequires:  go(github.com/caarlos0/env/v11)
BuildRequires:  go(github.com/gomodule/redigo)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/robfig/cron/v3)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/AdguardTeam/golibs) = %{version}

Requires:       go(github.com/c2h5oh/datasize)
Requires:       go(github.com/caarlos0/env/v11)
Requires:       go(github.com/gomodule/redigo)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/robfig/cron/v3)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/exp)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/text)

%description
Go utility packages primarily used in AdGuard projects.

%check -p
# http.ServeMux method routing requires httpmuxgo121=0 under GOPATH mode.
export GODEBUG=httpmuxgo121=0

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
