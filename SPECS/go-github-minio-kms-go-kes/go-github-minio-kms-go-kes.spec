# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kes
%define go_import_path  github.com/minio/kms-go/kes
%define upstream_tag    kes/v%{version}
# Client tests talk to a live KES/KMS endpoint.
%define go_test_ignore_failure 1

Name:           go-github-minio-kms-go-kes
Version:        0.3.1
Release:        %autorelease
Summary:        Go SDK for MinIO KES
License:        AGPL-3.0-only
URL:            https://github.com/minio/kms-go
#!RemoteAsset:  sha256:e78a33ced4a5cd2d14f912b75b64fcac24b7d261194f9646f9ce93a4578da6e1
Source0:        https://github.com/minio/kms-go/archive/refs/tags/%{upstream_tag}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(aead.dev/mem)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)

Provides:       go(github.com/minio/kms-go/kes) = %{version}

Requires:       go(aead.dev/mem)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)

%description
kes is the Go SDK for MinIO KES, a key-management sidecar. MinIO
imports github.com/minio/kms-go/kes. The older github.com/minio/kes-go
module is packaged separately.

%prep -a
# Nested module github.com/minio/kms-go/kes; go.mod lives under kes/.
find . -maxdepth 1 -mindepth 1 -not -name kes -not -name LICENSE -not -name README.md -exec rm -rf {} +
cp -a kes/. .
rm -rf kes

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
