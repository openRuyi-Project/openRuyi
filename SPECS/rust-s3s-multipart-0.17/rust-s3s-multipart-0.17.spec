# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name s3s-multipart
%global full_version 0.17.0
%global pkgname s3s-multipart-0.17

Name:           rust-s3s-multipart-0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Rust crate "s3s-multipart"
License:        Apache-2.0
URL:            https://github.com/Nugine/s3s
#!RemoteAsset:  sha256:a543079d42c20c81781b7e31704ecacd64b0e3819b2384db5bf4869abf6c6f01
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7/default) >= 0.7.8
Requires:       crate(bytes-1/default) >= 1.12.1
Requires:       crate(futures-core-0.3/default) >= 0.3.32
Requires:       crate(httparse-1/default) >= 1.10.1
Requires:       crate(memchr-2/default) >= 2.8.3
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "s3s-multipart"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
