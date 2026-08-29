# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bzip2-sys
%global full_version 0.1.13+1.0.8
%global pkgname bzip2-sys-0.1

Name:           rust-bzip2-sys-0.1
Version:        0.1.13
Release:        %autorelease
Summary:        Rust crate "bzip2-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/bzip2-rs
#!RemoteAsset:  sha256:225bff33b2141874fe80d71e07d6eec4f85c5c216453dd96388240f96e1acc14
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(pkg-config-0.3) >= 0.3.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/disabled) = %{version}
Provides:       crate(%{pkgname}/static) = %{version}

%description
Source code for takopackized Rust crate "bzip2-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
