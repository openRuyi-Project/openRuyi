# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           madmin-go
%define go_import_path  github.com/minio/madmin-go/v3

Name:           go-github-minio-madmin-go-v3
Version:        3.0.109
Release:        %autorelease
Summary:        MinIO administrative client library for Go
License:        AGPL-3.0-or-later
URL:            https://github.com/minio/madmin-go
#!RemoteAsset:  sha256:81d0b24e799f2289f0a7508f49c8017e4a7a9503cc7eb0b73c96dc1515e7c787
Source0:        https://github.com/minio/madmin-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport the upstream fix for a panic with prometheus/common >= 0.66.
Patch1000:      1000-initialize-prometheus-text-parser.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/golang-jwt/jwt/v4)
BuildRequires:  go(github.com/minio/minio-go/v7)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/prometheus/prom2json)
BuildRequires:  go(github.com/safchain/ethtool)
BuildRequires:  go(github.com/secure-io/sio-go)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/minio/madmin-go/v3) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/golang-jwt/jwt/v4)
Requires:       go(github.com/minio/minio-go/v7)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/prometheus/prom2json)
Requires:       go(github.com/safchain/ethtool)
Requires:       go(github.com/secure-io/sio-go)
Requires:       go(github.com/shirou/gopsutil/v3)
Requires:       go(github.com/tinylib/msgp)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(gopkg.in/yaml.v3)

%description
Go client library for administering MinIO services, including storage,
identity, configuration, monitoring and cluster operations.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
