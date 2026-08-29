# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros-backend
%global full_version 0.27.2
%global pkgname pyo3-macros-backend-0.27

Name:           rust-pyo3-macros-backend-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "pyo3-macros-backend"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:03b51720d314836e53327f5871d4c0cfb4fb37cc2c4a11cc71907a86342c40f9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1) >= 1.0.60
Requires:       crate(pyo3-build-config-0.27) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/default) >= 0.27.2
Requires:       crate(pyo3-build-config-0.27/resolve-config) >= 0.27.2
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
