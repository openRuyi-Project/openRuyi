# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ufmt
%global full_version 0.2.0
%global pkgname ufmt-0.2

Name:           rust-ufmt-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "ufmt"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/ufmt
#!RemoteAsset:  sha256:1a64846ec02b57e9108d6469d98d1648782ad6bb150a95a9baac26900bbeab9d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ufmt-macros-0.3/default) >= 0.3.0
Requires:       crate(ufmt-write-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for the Rust crate "ufmt"

%package     -n %{name}+std
Summary:        (6-40x) smaller, (2-9x) faster and panic-free alternative to `core::fmt` - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ufmt-write-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ufmt crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-APACHE LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
