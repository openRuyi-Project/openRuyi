# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fastrand
%global full_version 1.9.0
%global pkgname fastrand-1

Name:           rust-fastrand-1
Version:        1.9.0
Release:        %autorelease
Summary:        Rust crate "fastrand"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/fastrand
#!RemoteAsset:  sha256:e51093e27b0797c359783294ca4f0a911c270184cb10f85783b118614a1501be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(instant-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fastrand"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
