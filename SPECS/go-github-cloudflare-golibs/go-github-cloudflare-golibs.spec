# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golibs
%define go_import_path  github.com/cloudflare/golibs
# This standalone historical benchmark depends on the pre-module
# github.com/youtube/vitess import path and is unrelated to the libraries. KT
# tests require external Kyoto Tycoon server processes. The spacesaving tools
# directory contains several independent main programs and is not one package.
%define go_test_exclude %{shrink:
    %{go_import_path}/kt
    %{go_import_path}/lrucache/benchmark
    %{go_import_path}/spacesaving/tools
}
%define commit_id       558c04120a4eb7c3f8b5847da1a2df2bc9b7ddac

Name:           go-github-cloudflare-golibs
Version:        0+git20260819.558c041
Release:        %autorelease
Summary:        Collection of small Go libraries from Cloudflare
License:        BSD-3-Clause
URL:            https://github.com/cloudflare/golibs
#!RemoteAsset:  sha256:2fdc9c01be3b9fed060f636b99df56c430ed1ab1a9aa42e21cc26f426ac54e77
Source0:        https://github.com/cloudflare/golibs/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit_id}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/miekg/pcap)
BuildRequires:  go(github.com/opentracing/opentracing-go)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  libpcap-devel

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/miekg/dns)
Requires:       go(github.com/miekg/pcap)
Requires:       go(github.com/opentracing/opentracing-go)
Requires:       go(github.com/prometheus/client_golang)

%description
Golibs contains reusable Cloudflare packages for caching, buffering, pooling,
rate limiting, metrics, and related infrastructure tasks.

%check -a
go test -vet=off -c -o /dev/null %{go_import_path}/kt

%files
%doc README.md
%license LICENSE-BSD-CloudFlare
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
