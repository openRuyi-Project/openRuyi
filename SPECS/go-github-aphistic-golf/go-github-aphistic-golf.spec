# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golf
%define go_import_path  github.com/aphistic/golf
%global commit_id       02c07f170c5a8a0300a199a10bb04a55c721c017

Name:           go-github-aphistic-golf
Version:        0+git20261020.02c07f1
Release:        %autorelease
Summary:        GELF logging library for Go
License:        MIT
URL:            https://github.com/aphistic/golf
#!RemoteAsset:  sha256:0cb1378c66edeba952260e2d92c7a1d2737907ab94db218b81499e6b01851566
Source0:        https://github.com/aphistic/golf/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n golf-%{commit_id}

# Tests intentionally pass missing or invalid printf arguments; go vet reports
# genMsg format %2b reads arg #1, but call has 0 args, among similar cases.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/aphistic/sweet)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/onsi/gomega)

Provides:       go(github.com/aphistic/golf) = %{version}

Requires:       go(github.com/google/uuid)

%description
Golf sends log messages in the Graylog Extended Log Format (GELF).
It supports TCP, UDP, and TLS transports.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
