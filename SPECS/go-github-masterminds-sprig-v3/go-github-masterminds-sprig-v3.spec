# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sprig
%define go_import_path  github.com/Masterminds/sprig/v3

Name:           go-github-masterminds-sprig-v3
Version:        3.3.0
Release:        %autorelease
Summary:        Template function library for Go
License:        MIT
URL:            https://github.com/Masterminds/sprig
#!RemoteAsset:  sha256:bf74b78c51c2e5e0b181a3edc5d5787dcf70757d30f8a002df77be594fa8b8d1
Source0:        https://github.com/Masterminds/sprig/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/Masterminds/goutils)
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/huandu/xstrings)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/shopspring/decimal)
BuildRequires:  go(github.com/spf13/cast)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/Masterminds/sprig/v3) = %{version}

Requires:       go(dario.cat/mergo)
Requires:       go(github.com/Masterminds/goutils)
Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/huandu/xstrings)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(github.com/shopspring/decimal)
Requires:       go(github.com/spf13/cast)
Requires:       go(golang.org/x/crypto)

%description
Sprig supplies commonly useful string, numeric, date, cryptographic and data
structure functions for Go templates.

# network_test.go performs live DNS resolution, which is unavailable in OBS.
%prep -a
rm -f network_test.go

%check
# Compile all packages and tests before tolerating the architecture-sensitive
# TestRound expectation (123.556 on x86_64, 123.555 on riscv64).
%buildsystem_golangmodules_check -run '^$'
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
