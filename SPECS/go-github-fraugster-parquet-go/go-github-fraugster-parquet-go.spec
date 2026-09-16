# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           parquet-go
%define go_import_path  github.com/fraugster/parquet-go

Name:           go-github-fraugster-parquet-go
Version:        0.12.0
Release:        %autorelease
Summary:        Go implementation of the Apache Parquet file format
License:        Apache-2.0
URL:            https://github.com/fraugster/parquet-go
#!RemoteAsset:  sha256:e09b75b3b0647153df603cdb585a70c8ef239f2ab099af947351a63abc5c148e
Source0:        https://github.com/fraugster/parquet-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apache/thrift)
BuildRequires:  go(github.com/araddon/dateparse)
BuildRequires:  go(github.com/golang/snappy)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/fraugster/parquet-go) = %{version}

Requires:       go(github.com/apache/thrift)
Requires:       go(github.com/araddon/dateparse)
Requires:       go(github.com/golang/snappy)

%description
parquet-go reads and writes Apache Parquet files in Go. MinIO uses it
to handle Parquet objects.

%prep -a
# compatibility/ is a Java/Docker interop harness, not the library.
rm -rf compatibility
# cmd/parquet-tool and cmd/csv2parquet are inspection helpers, not
# upstream-distributed programs. This RPM is the importable library.
rm -rf cmd

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
