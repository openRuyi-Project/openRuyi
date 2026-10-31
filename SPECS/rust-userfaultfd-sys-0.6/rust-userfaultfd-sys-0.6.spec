# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name userfaultfd-sys
%global full_version 0.6.0
%global pkgname userfaultfd-sys-0.6

Name:           rust-userfaultfd-sys-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "userfaultfd-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/bytecodealliance/userfaultfd-rs
#!RemoteAsset:  sha256:dc91d95a797a81604af22946d0e86656f27feb0b9665c60665cf3554df12d1a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bindgen-0.69) >= 0.69.2
Requires:       crate(bindgen-0.69/runtime) >= 0.69.2
Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/linux4-14) = %{version}
Provides:       crate(%{pkgname}/linux5-13) = %{version}
Provides:       crate(%{pkgname}/linux5-7) = %{version}

%description
Source code for takopackized Rust crate "userfaultfd-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
