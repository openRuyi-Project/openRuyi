# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           common
%define go_import_path  github.com/prometheus/common
# Circular dependency with github.com/prometheus/client_golang
%define go_test_exclude_glob github.com/prometheus/common/config*

Name:           go-github-prometheus-common
Version:        0.67.5
Release:        %autorelease
Summary:        Go libraries shared across Prometheus components and libraries.
License:        Apache-2.0
URL:            https://github.com/prometheus/common
#!RemoteAsset
Source0:        https://github.com/prometheus/common/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/golang-jwt/jwt/v5)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/julienschmidt/httprouter)
BuildRequires:  go(github.com/munnerz/goautoneg)
BuildRequires:  go(github.com/mwitkow/go-conntrack)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/prometheus/common) = %{version}

Requires:       go(github.com/alecthomas/kingpin/v2)
Requires:       go(github.com/golang-jwt/jwt/v5)
Requires:       go(github.com/google/go-cmp)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/julienschmidt/httprouter)
Requires:       go(github.com/munnerz/goautoneg)
Requires:       go(github.com/mwitkow/go-conntrack)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/stretchr/testify)
Requires:       go(gopkg.in/yaml.v2)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(google.golang.org/protobuf)

%description
This repository contains Go libraries that are shared across Prometheus
components and libraries. They are considered internal to Prometheus,
without any stability guarantees for external usage.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
