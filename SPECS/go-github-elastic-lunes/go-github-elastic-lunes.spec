# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lunes
%define go_import_path  github.com/elastic/lunes

Name:           go-github-elastic-lunes
Version:        0.2.2
Release:        %autorelease
Summary:        Localized time parser for Go
License:        Apache-2.0
URL:            https://github.com/elastic/lunes
#!RemoteAsset:  sha256:922a635e4807ceda1d4c3638442f1f8623f35f61935cff5eaed820cef611699a
Source0:        https://github.com/elastic/lunes/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/goodsign/monday)
BuildRequires:  go(github.com/magefile/mage)
BuildRequires:  tzdata

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/magefile/mage)

%description
Lunes translates localized Gregorian date and time values before parsing them
with Go's standard time package.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
