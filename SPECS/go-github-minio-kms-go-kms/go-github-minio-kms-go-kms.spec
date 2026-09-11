# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kms
%define go_import_path  github.com/minio/kms-go/kms
%define commit_id       4e64ce8d0f35ed659422a1c70ae4dd152d106913
# Client tests talk to a live KMS endpoint.
%define go_test_ignore_failure 1

Name:           go-github-minio-kms-go-kms
Version:        0+git20260908.4e64ce8
Release:        %autorelease
Summary:        Go SDK for MinIO KMS
License:        AGPL-3.0-only
URL:            https://github.com/minio/kms-go
#!RemoteAsset:  sha256:a87233ba3098e166469346ff3bf4ecef0a53250cbbb4175c272af14920844a95
Source0:        https://github.com/minio/kms-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(aead.dev/mem)
BuildRequires:  go(aead.dev/mtls)
BuildRequires:  go(google.golang.org/protobuf)

Provides:       go(github.com/minio/kms-go/kms) = %{version}

Requires:       go(aead.dev/mem)
Requires:       go(aead.dev/mtls)
Requires:       go(google.golang.org/protobuf)

%description
kms is the Go SDK for MinIO KMS. MinIO pins commit 4e64ce8 (no kms/v0.5.1
tag). The older github.com/minio/kms-go root module is packaged
separately.

%prep -a
# Nested module github.com/minio/kms-go/kms; go.mod lives under kms/.
find . -maxdepth 1 -mindepth 1 -not -name kms -not -name LICENSE -not -name README.md -exec rm -rf {} +
cp -a kms/. .
rm -rf kms

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
