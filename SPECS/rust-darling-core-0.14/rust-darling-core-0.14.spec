# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name darling_core
%global full_version 0.14.4
%global pkgname darling-core-0.14

Name:           rust-darling-core-0.14
Version:        0.14.4
Release:        %autorelease
Summary:        Rust crate "darling_core"
License:        MIT
URL:            https://github.com/TedDriggs/darling
#!RemoteAsset:  sha256:109c1ca6e6b7f82cc233a97004ea8ed7ca123a9af07a8230878fcfda9b158bf0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.7
Requires:       crate(ident-case-1/default) >= 1.0.1
Requires:       crate(proc-macro2-1/default) >= 1.0.37
Requires:       crate(quote-1/default) >= 1.0.18
Requires:       crate(syn-1/default) >= 1.0.91
Requires:       crate(syn-1/extra-traits) >= 1.0.91
Requires:       crate(syn-1/full) >= 1.0.91

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/diagnostics) = %{version}

%description
Use https://crates.io/crates/darling in your code.
Source code for takopackized Rust crate "darling_core"

%package     -n %{name}+strsim
Summary:        Helper crate for proc-macro library for reading attributes into structs when implementing custom derives - feature "strsim" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(strsim-0.10/default) >= 0.10.0
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
