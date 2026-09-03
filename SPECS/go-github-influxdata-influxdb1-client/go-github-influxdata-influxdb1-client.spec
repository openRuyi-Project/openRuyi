# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           influxdb1-client
%define go_import_path  github.com/influxdata/influxdb1-client
%define commit_id       a9ab5670611c9764d02779d2121f9a1240c1a867

Name:           go-github-influxdata-influxdb1-client
Version:        0+git20260818.a9ab567
Release:        %autorelease
Summary:        InfluxDB 1.x client library for Go
License:        MIT
URL:            https://github.com/influxdata/influxdb1-client
#!RemoteAsset:  sha256:43079770260eb68826497bf5b3e472b531b31e9552b7c0400926e6adaf4ed2ec
Source0:        https://github.com/influxdata/influxdb1-client/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.26 vet rejects two legacy non-constant fmt.Errorf calls in the root
# package; keep the complete test suite enabled. - HNO3Miracle
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/v2) = %{version}

%description
The influxdb1-client repository provides the deprecated InfluxDB 1.x client
library, including its v2 import path.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
