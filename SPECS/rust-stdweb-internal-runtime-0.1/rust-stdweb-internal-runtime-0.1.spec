# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stdweb-internal-runtime
%global full_version 0.1.5
%global pkgname stdweb-internal-runtime-0.1

Name:           rust-stdweb-internal-runtime-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "stdweb-internal-runtime"
License:        MIT OR Apache-2.0
URL:            https://github.com/koute/stdweb
#!RemoteAsset:  sha256:213701ba3370744dcd1a12960caa4843b3d68b4d1c0a5d575e0d65b2ee9d16c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/docs-rs) = %{version}

%description
Source code for takopackized Rust crate "stdweb-internal-runtime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
