# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hystrix-go
%define go_import_path  github.com/afex/hystrix-go
%define commit_id       fa1af6a1f4f56e0e50d427fe901cd604d8c6fb8a

Name:           go-github-afex-hystrix-go
Version:        0+git20260818.fa1af6a
Release:        %autorelease
Summary:        Circuit breaker and fault tolerance library for Go
License:        MIT
URL:            https://github.com/afex/hystrix-go
#!RemoteAsset:  sha256:45d6aa4f0571c1720748998a1cdeca357b7de895c4f39b10de4db8645aa19b76
Source0:        https://github.com/afex/hystrix-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/datadog-go)
BuildRequires:  go(github.com/cactus/go-statsd-client)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/smartystreets/goconvey)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/DataDog/datadog-go)
Requires:       go(github.com/cactus/go-statsd-client)
Requires:       go(github.com/rcrowley/go-metrics)

%description
Hystrix-go provides circuit breaker and fault tolerance patterns for Go
services.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
