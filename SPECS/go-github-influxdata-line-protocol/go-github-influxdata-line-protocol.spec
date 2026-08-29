# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           line-protocol
%define go_import_path  github.com/influxdata/line-protocol
%define commit_id 2487e7298839615811464221244c572dc05b50ad

Name:           go-github-influxdata-line-protocol
Version:        0+git20260605.2487e729
Release:        %autorelease
Summary:        InfluxDB line protocol codec for Go
License:        MIT
URL:            https://github.com/influxdata/line-protocol
#!RemoteAsset:  sha256:377f4303387074ceeb50e60c3a784abb4b07d7db850ac35513d252fbb05e7ef0
Source0:        https://github.com/influxdata/line-protocol/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/influxdata/line-protocol) = %{version}

%description
InfluxDB line-protocol codec

This module implements a high performance Go codec for the line-protocol
syntax as accepted by InfluxDB. Currently the API is low level - it's
intended for converting line-protocol to some chosen concrete types that
aren't specified here. (In future work, we'll define a Point type that
implements a convenient but less performant type to encode or decode).

The API documentation is here:
(https://pkg.go.dev/github.com/influxdata/line-protocol/v2/lineprotocol)

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
