# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-error
%global full_version 1.0.4
%global pkgname proc-macro-error-1

Name:           rust-proc-macro-error-1
Version:        1.0.4
Release:        %autorelease
Summary:        Rust crate "proc-macro-error"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/CreepySkeleton/proc-macro-error
#!RemoteAsset:  sha256:da25490ff9892aab3fcf7c36f08cfb902dd3e71ca0f9f9517bea02a73a5ce38c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-error-attr-1/default) >= 1.0.4
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(version-check-0.9) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-error"

%package     -n %{name}+syn
Summary:        Almost drop-in replacement to panics in proc-macros - feature "syn" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-1) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/syn) = %{version}
Provides:       crate(%{pkgname}/syn-error) = %{version}

%description -n %{name}+syn
This metapackage enables feature "syn" for the Rust proc-macro-error crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "syn-error" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
