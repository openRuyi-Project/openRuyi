# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-118-fuzz-build
%define go_import_path  github.com/AdamKorcz/go-118-fuzz-build
%define commit          a70c2aa677fa43583571959478decabe02a96cd6

Name:           go-github-adamkorcz-go-118-fuzz-build
Version:        0+git20261016.a70c2aa677fa
Release:        %autorelease
Summary:        Go source helpers for compiling native fuzzers with libFuzzer
License:        Apache-2.0
URL:            https://github.com/AdamKorcz/go-118-fuzz-build
#!RemoteAsset:  sha256:18b185bb5f6172d622c9306e8f68602dedd2b946dd9ac35cb2dc1f5bc65bebb4
Source0:        https://github.com/AdamKorcz/go-118-fuzz-build/archive/a70c2aa677fa.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/AdaLogics/go-fuzz-headers)
BuildRequires:  go(github.com/cyphar/filepath-securejoin)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/AdamKorcz/go-118-fuzz-build) = %{version}
Provides:       go(github.com/AdamKorcz/go-118-fuzz-build/coverage) = %{version}
Provides:       go(github.com/AdamKorcz/go-118-fuzz-build/testing) = %{version}

Requires:       go(github.com/AdaLogics/go-fuzz-headers)
Requires:       go(github.com/cyphar/filepath-securejoin)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)

%description
This package contains the Go source for adapting native Go fuzz harnesses
to libFuzzer, including compatible testing and coverage helpers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
