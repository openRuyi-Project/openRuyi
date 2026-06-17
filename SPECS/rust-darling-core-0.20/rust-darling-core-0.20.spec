# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name darling_core
%global full_version 0.20.11
%global pkgname darling-core-0.20

Name:           rust-darling-core-0.20
Version:        0.20.11
Release:        %autorelease
Summary:        Rust crate "darling_core"
License:        MIT
URL:            https://github.com/TedDriggs/darling
#!RemoteAsset:  sha256:0d00b9596d185e565c2207a0b01f8bd1a135483d02d9b7b0a54b11da8d53412e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.7
Requires:       crate(ident-case-1/default) >= 1.0.1
Requires:       crate(proc-macro2-1/default) >= 1.0.86
Requires:       crate(quote-1/default) >= 1.0.18
Requires:       crate(syn-2/default) >= 2.0.15
Requires:       crate(syn-2/extra-traits) >= 2.0.15
Requires:       crate(syn-2/full) >= 2.0.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/diagnostics) = %{version}

%description
Use https://crates.io/crates/darling in your code.
Source code for takopackized Rust crate "darling_core"

%package     -n %{name}+strsim
Summary:        Helper crate for proc-macro library for reading attributes into structs when implementing custom derives - feature "strsim" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(strsim-0.11/default) >= 0.11.1
Provides:       crate(%{pkgname}/strsim) = %{version}
Provides:       crate(%{pkgname}/suggestions) = %{version}

%description -n %{name}+strsim
Use https://crates.io/crates/darling in your code.
This metapackage enables feature "strsim" for the Rust darling_core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "suggestions" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
