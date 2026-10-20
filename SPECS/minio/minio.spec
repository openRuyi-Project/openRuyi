# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           minio
%define go_import_path  github.com/minio/minio
%define MinIO_VERSION   2025-10-15T17-29-55Z
%define commit_id       9e49d5e7a648f00e26f2246f4dc28e6b07f8c84a
# These cases resolve external example domains, unavailable in offline builds.
%define minio_skip_dns ^TestGetLocalPeer$|^TestGetRemotePeers$|^TestNewEndpoint$/^case-1$|^TestCreateEndpoints$/^#1[0-3]$|^TestCheckLocalServerAddr$/^#06$

Name:           minio
Version:        2025.10.15T17.29.55Z
Release:        %autorelease
Summary:        High-performance S3-compatible object storage
License:        AGPL-3.0-or-later
URL:            https://github.com/minio/minio
#!RemoteAsset:  sha256:be6d0bd3696c3a13a35f02d3a0280b64319c67918b4501c5c3d87f96d000085c
Source0:        https://github.com/minio/minio/archive/refs/tags/RELEASE.%{MinIO_VERSION}.tar.gz
# TODO: Use vendor mode for now. use build dependencies later  - Julian
#!RemoteAsset:  sha256:ec02eb0bd1b203d7df8a60238af135de850dacc3808811046fa8bbf953fa75c0
Source1:        https://github.com/software-vendor/go-minio-vendor/releases/download/RELEASE.%{MinIO_VERSION}/minio-RELEASE.%{MinIO_VERSION}-vendor.tar.gz
Source2:        minio.service
Source3:        minio.sysconfig
Source4:        minio.sysusers
Source5:        README.openruyi
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  systemd-rpm-macros

Provides:       user(minio)
Provides:       group(minio)

Requires(pre):  systemd-sysusers

%description
MinIO is a high-performance, S3-compatible object storage solution released under the GNU AGPL v3.0 license. Designed for speed and scalability, it powers AI/ML, analytics, and data-intensive workloads with industry-leading performance.

%prep -a
%setup -q -D -T -a 1 -n %{name}-%{version}

%build
# The Go buildsystem currently forces GOPATH mode; this package still uses vendor.
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOPROXY=off
export GOTOOLCHAIN=local
export GOFLAGS="-buildmode=pie -mod=vendor -trimpath -modcacherw"
go build -v -ldflags "-X github.com/minio/minio/cmd.Version=2025-10-15T17:29:55Z -X github.com/minio/minio/cmd.ReleaseTag=RELEASE.%{MinIO_VERSION} -X github.com/minio/minio/cmd.CommitID=%{commit_id} -X github.com/minio/minio/cmd.ShortCommitID=9e49d5e7a648 -X github.com/minio/minio/cmd.CopyrightYear=2025" -o %{_name} .

%install -a
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/minio.service
install -D -m 0600 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/minio
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/minio.conf
install -d -m 0750 %{buildroot}%{_sharedstatedir}/minio
cp %{SOURCE5} README.openruyi

%check
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOPROXY=off
export GOTOOLCHAIN=local
export GOFLAGS="-mod=vendor -trimpath -modcacherw"
go test -v -timeout=30m -skip '%{minio_skip_dns}' ./...
%{buildroot}%{_bindir}/minio --version | tee minio-version.txt
grep -F 'RELEASE.%{MinIO_VERSION}' minio-version.txt
grep -F '%{commit_id}' minio-version.txt

%pre
%sysusers_create_package %{name} %{SOURCE4}

%post
%systemd_post minio.service

%preun
%systemd_preun minio.service

%postun
%systemd_postun_with_restart minio.service

%files
%doc README*
%license LICENSE*
%{_bindir}/%{_name}
%{_unitdir}/minio.service
%{_sysusersdir}/minio.conf
%config(noreplace) %attr(0600, root, root) %{_sysconfdir}/sysconfig/minio
%dir %attr(0750, minio, minio) %{_sharedstatedir}/minio

%changelog
%autochangelog
