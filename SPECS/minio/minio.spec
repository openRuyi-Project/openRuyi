# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           minio
%define go_import_path  github.com/minio/minio
%define MinIO_VERSION 2025-10-15T17-29-55Z
# Test failure due to network connection part
%define go_test_ignore_failure 1

Name:           minio
Version:        2025.10.15T17.29.55Z
Release:        %autorelease
Summary:        MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.
License:        AGPL-3.0 license
URL:            https://github.com/minio/minio
#!RemoteAsset
Source0:        https://github.com/minio/minio/archive/refs/tags/RELEASE.%{MinIO_VERSION}.tar.gz
# TODO: Use vendor mode for now. use build dependencies later  - Julian
#!RemoteAsset
Source1:        https://github.com/software-vendor/go-minio-vendor/releases/download/RELEASE.%{MinIO_VERSION}/minio-RELEASE.%{MinIO_VERSION}-vendor.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros

%description
MinIO is a high-performance, S3-compatible object storage solution released under the GNU AGPL v3.0 license. Designed for speed and scalability, it powers AI/ML, analytics, and data-intensive workloads with industry-leading performance.

%prep -a
%setup -q -D -T -a 1 -n %{name}-%{version}

%build
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOFLAGS="-buildmode=pie -mod=vendor -trimpath -modcacherw"
go build -v -o %{_name} .

%install
install -D -m 0755 %{_name} %{buildroot}%{_bindir}/%{_name}

%check
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
# TODO: go_test_ignore_failure manually without buildsystem - Julian
go test -v ./... || :

%files
%license LICENSE*
%doc README*
%{_bindir}/%{_name}

%changelog
%autochangelog
