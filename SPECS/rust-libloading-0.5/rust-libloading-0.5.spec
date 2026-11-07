# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libloading
%global full_version 0.5.2
%global pkgname libloading-0.5

Name:           rust-libloading-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "libloading"
License:        ISC
URL:            https://github.com/nagisa/rust_libloading/
#!RemoteAsset:  sha256:f2b111a074963af1d37a139918ac6d49ad1d0d5e47f72fd55388619691a7d753
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.0
Requires:       crate(winapi-0.3/libloaderapi) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libloading"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
