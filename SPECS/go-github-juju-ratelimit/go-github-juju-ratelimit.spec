# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ratelimit
%define go_import_path  github.com/juju/ratelimit

Name:           go-github-juju-ratelimit
Version:        1.0.2
Release:        %autorelease
Summary:        Token-bucket rate limiter for Go
License:        LGPL-3.0-only
URL:            https://github.com/juju/ratelimit
#!RemoteAsset:  sha256:53eaae8378cdce878e82851ecf01dcd63564ad2211309e7c61bd36a84f14cbbc
Source0:        https://github.com/juju/ratelimit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(github.com/juju/ratelimit) = %{version}

%description
ratelimit is an efficient token-bucket implementation for limiting
the rate of arbitrary events.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
