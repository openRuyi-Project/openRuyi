# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde-untagged
%global full_version 0.1.9
%global pkgname serde-untagged-0.1

Name:           rust-serde-untagged-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "serde-untagged"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/serde-untagged
#!RemoteAsset:  sha256:f9faf48a4a2d2693be24c6289dbe26552776eb7737074e6722891fadbe6c5058
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(erased-serde-0.4/alloc) >= 0.4.2
Requires:       crate(serde-1) >= 1.0.220
Requires:       crate(serde-core-1/alloc) >= 1.0.220
Requires:       crate(typeid-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "serde-untagged"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
