# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           csvparser
%define go_import_path  github.com/minio/csvparser

Name:           go-github-minio-csvparser
Version:        1.0.0
Release:        %autorelease
Summary:        Package csv reads and writes comma-separated values (CSV) files.
License:        BSD-3-Clause
URL:            https://github.com/minio/csvparser
#!RemoteAsset
Source0:        https://github.com/minio/csvparser/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/minio/csvparser) = %{version}

%description
This package is forked from encoding/csv from Go upstream, original
package is under feature freeze and we had to expand the scope of CSV
RFC for S3 Select CSV support.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
