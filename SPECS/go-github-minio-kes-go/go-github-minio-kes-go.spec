# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kes-go
%define go_import_path  github.com/minio/kes-go

Name:           go-github-minio-kes-go
Version:        0.2.1
Release:        %autorelease
Summary:        MinIO Key Managment SDK
License:        AGPL-3.0
URL:            https://github.com/minio/kes-go
#!RemoteAsset
Source0:        https://github.com/minio/kes-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(aead.dev/mem)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)

Provides:       go(github.com/minio/kes-go) = %{version}

%description
MinIO KMS

This repository contains the Go SDKs for MinIO KMS and MinIO KES in two
separate Go modules:

 * kms-go/kms contains the KMS Go SDK
 * kms-go/kes contains the KES Go SDK

Each module uses its own semantic version and can be imported
separately.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
