# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fasthttp
%define go_import_path  github.com/valyala/fasthttp
# Skip network tests: lookup github.com on [::1]:53: connection refused.
%define go_test_exclude github.com/valyala/fasthttp/fasthttpproxy

Name:           go-github-valyala-fasthttp
Version:        1.69.0
Release:        %autorelease
Summary:        Fast HTTP server and client API for Go
License:        MIT
URL:            https://github.com/valyala/fasthttp
#!RemoteAsset:  sha256:623a66903b78637f1686749fc4f6d3fb239eddfd25629a006e3b53fea9624db1
Source0:        https://github.com/valyala/fasthttp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects upstream mismatched format strings.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/andybalholm/brotli)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/valyala/bytebufferpool)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/valyala/fasthttp) = %{version}

Requires:       go(github.com/andybalholm/brotli)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/valyala/bytebufferpool)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
Fasthttp provides high-performance HTTP server and client implementations for
Go applications with demanding throughput and latency requirements.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
