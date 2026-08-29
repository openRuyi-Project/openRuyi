# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dav1d
%global full_version 0.11.1
%global pkgname dav1d-0.11

Name:           rust-dav1d-0.11
Version:        0.11.1
Release:        %autorelease
Summary:        Rust crate "dav1d"
License:        MIT
URL:            https://github.com/rust-av/dav1d-rs
#!RemoteAsset:  sha256:3ee89cb860616069c67520dcd66cacdb900b57c799f634a0eb6d91f6e2a82b61
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(av-data-0.4/default) >= 0.4.2
Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(dav1d-sys-0.8/default) >= 0.8.2
Requires:       crate(static-assertions-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dav1d"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
