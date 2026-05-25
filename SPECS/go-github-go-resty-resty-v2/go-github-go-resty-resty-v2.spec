# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           resty
%define go_import_path  github.com/go-resty/resty/v2

Name:           go-github-go-resty-resty-v2
Version:        2.17.2
Release:        %autorelease
Summary:        Simple HTTP, REST, and SSE client library for Go
License:        MIT
URL:            https://github.com/go-resty/resty
#!RemoteAsset:  sha256:1548d7af5e8236ec394b672f603f3bd3f89211cdc69e26bb62f5117a42d10e74
Source0:        https://github.com/go-resty/resty/archive/refs/tags/v2.17.2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n resty-2.17.2

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/net/proxy)
BuildRequires:  go(golang.org/x/net/publicsuffix)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(golang.org/x/time/rate)

Provides:       go(github.com/go-resty/resty/v2) = %{version}
Provides:       go(github.com/go-resty/resty/v2/shellescape) = %{version}

Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/net/publicsuffix)


%description
Simple HTTP, REST, and SSE client library for Go
Documentation

Go to (https://resty.dev) and refer to godoc.

Minimum Go Version

Use go1.23 and above.

Support & Donate


%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
