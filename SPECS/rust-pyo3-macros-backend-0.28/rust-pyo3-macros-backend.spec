# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros-backend
%global full_version 0.28.3
%global pkgname pyo3-macros-backend-0.28

Name:           rust-pyo3-macros-backend-0.28
Version:        0.28.3
Release:        %autorelease
Summary:        Rust crate "pyo3-macros-backend"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:c4cdc218d835738f81c2338f822078af45b4afdf8b2e33cbb5916f108b813acb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(pyo3-build-config-0.28/default) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(quote-1.0) >= 1.0.45
Requires:       crate(syn-2.0/clone-impls) >= 2.0.117
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(syn-2.0/visit-mut) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-async)
Provides:       crate(%{pkgname}/experimental-inspect)

%description
Source code for takopackized Rust crate "pyo3-macros-backend"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
