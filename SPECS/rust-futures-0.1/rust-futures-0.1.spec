# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures
%global full_version 0.1.31
%global pkgname futures-0.1

Name:           rust-futures-0.1
Version:        0.1.31
Release:        %autorelease
Summary:        Rust crate "futures"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/futures-rs
#!RemoteAsset:  sha256:3a471a38ef8ed83cd6e40aa59c1ffe17db6855c18e3604d9c4ed8c08ebc28678
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}
Provides:       crate(%{pkgname}/with-deprecated) = %{version}

%description
Source code for takopackized Rust crate "futures"

%package     -n %{name}+default
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/use-std) = %{version}
Requires:       crate(%{pkgname}/with-deprecated) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
