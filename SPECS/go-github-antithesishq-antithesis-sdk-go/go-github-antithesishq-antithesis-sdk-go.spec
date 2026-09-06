# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           antithesis-sdk-go
%define go_import_path  github.com/antithesishq/antithesis-sdk-go
%define upstream_version 0.7.2-default-no-op
# The assertion scanner tests create temporary modules and invoke go mod, but
# the distribution Go test macro intentionally runs in GOPATH mode.
%define go_test_exclude %{go_import_path}/tools/antithesis-go-instrumentor %{go_import_path}/tools/antithesis-go-instrumentor/scanners/assertions

Name:           go-github-antithesishq-antithesis-sdk-go
Version:        0.7.2~default.no.op
Release:        %autorelease
Summary:        Go SDK for the Antithesis platform
License:        MIT
URL:            https://github.com/antithesishq/antithesis-sdk-go
#!RemoteAsset:  sha256:3be271331a1733975f0434d4d79a032efea70b9195efce2a0244ad43ad5ac939
Source0:        https://github.com/antithesishq/antithesis-sdk-go/archive/v%{upstream_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-quicktest/qt)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/tools)

%description
The Antithesis Go SDK provides APIs for assertions, randomness, and lifecycle
control in Antithesis simulations. This package uses the default no-op build.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
