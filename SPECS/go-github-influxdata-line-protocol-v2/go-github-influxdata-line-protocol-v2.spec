# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           line-protocol
%define go_import_path  github.com/influxdata/line-protocol/v2

Name:           go-github-influxdata-line-protocol-v2
Version:        2.2.1
Release:        %autorelease
Summary:        InfluxDB line protocol codec for Go
License:        MIT
URL:            https://github.com/influxdata/line-protocol
#!RemoteAsset:  sha256:38cef425ce233b4e195ac2416f4627538daedd0e4cec3de86c0a2d949ab71135
Source0:        https://github.com/influxdata/line-protocol/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# corpus_test.go needs github.com/influxdata/line-protocol-corpus, while
# that corpus package also needs this module; skip only the corpus tests to
# break the bootstrap cycle and keep the rest of %check enabled. A subpackage
# would not solve this because the corpus is a separate upstream source/import
# path and cannot be available during this package's %check before the corpus
# package itself is built.
# - HNO3Miracle
Patch2000:      2000-disable-corpus-test-bootstrap-cycle.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/frankban/quicktest)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)

Provides:       go(github.com/influxdata/line-protocol/v2) = %{version}

%description
This module implements a high performance Go codec for the line protocol
syntax accepted by InfluxDB.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
