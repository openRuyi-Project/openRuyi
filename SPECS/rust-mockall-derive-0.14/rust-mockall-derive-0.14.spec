# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mockall_derive
%global full_version 0.14.0
%global pkgname mockall-derive-0.14

Name:           rust-mockall-derive-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "mockall_derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/asomers/mockall
#!RemoteAsset:  sha256:ca41ce716dda6a9be188b385aa78ee5260fc25cd3802cb2a8afdc6afbe6b6dbf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.75
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-2/default) >= 2.0.52
Requires:       crate(syn-2/extra-traits) >= 2.0.52
Requires:       crate(syn-2/full) >= 2.0.52
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mockall_derive"

%package     -n %{name}+nightly-derive
Summary:        Procedural macros for Mockall - feature "nightly_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/nightly) >= 1.0.75
Provides:       crate(%{pkgname}/nightly-derive) = %{version}

%description -n %{name}+nightly-derive
This metapackage enables feature "nightly_derive" for the Rust mockall_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
