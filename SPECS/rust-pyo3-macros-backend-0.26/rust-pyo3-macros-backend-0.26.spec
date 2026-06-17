# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros-backend
%global full_version 0.26.0
%global pkgname pyo3-macros-backend-0.26

Name:           rust-pyo3-macros-backend-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "pyo3-macros-backend"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:100246c0ecf400b475341b8455a9213344569af29a3c841d29270e53102e0fcf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1) >= 1.0.60
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/default) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-2/clone-impls) >= 2.0.59
Requires:       crate(syn-2/derive) >= 2.0.59
Requires:       crate(syn-2/extra-traits) >= 2.0.59
Requires:       crate(syn-2/full) >= 2.0.59
Requires:       crate(syn-2/parsing) >= 2.0.59
Requires:       crate(syn-2/printing) >= 2.0.59
Requires:       crate(syn-2/visit-mut) >= 2.0.59
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/experimental-async) = %{version}
Provides:       crate(%{pkgname}/experimental-inspect) = %{version}

%description
Source code for takopackized Rust crate "pyo3-macros-backend"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
