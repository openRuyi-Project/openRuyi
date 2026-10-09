# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           s3cli
%define go_import_path  yunion.io/x/s3cli
%define commit_id       1c11599d28e1d002a8fc55829d23539a3b8cd276

Name:           go-yunion-x-s3cli
Version:        0+git20260922.1c11599
Release:        %autorelease
Summary:        Yunion S3 client library for Go
License:        Apache-2.0
URL:            https://github.com/yunionio/s3cli
#!RemoteAsset:  sha256:ca7307046ccb107fbbd990f90fca5d1ecc11a8ef4200abf42067004d51874d1b
Source0:        https://github.com/yunionio/s3cli/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
# The fork retains Apache-2.0 source headers but omits the license file.
# License text from https://github.com/minio/minio-go/blob/v6.0.33/LICENSE
Source1:        LICENSE
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/minio/minio-go/v6)
BuildRequires:  go(golang.org/x/net)

Provides:       go(yunion.io/x/s3cli) = %{version}

Requires:       go(github.com/minio/minio-go/v6)
Requires:       go(golang.org/x/net)

%description
This package provides Yunion's fork of the MinIO Go client library for
S3 compatible object storage.

%prep -a
cp %{SOURCE1} LICENSE

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
