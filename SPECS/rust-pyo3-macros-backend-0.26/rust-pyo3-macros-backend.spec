# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1.0) >= 1.0.81
Requires:       crate(pyo3-build-config-0.26/default) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(quote-1.0) >= 1.0.36
Requires:       crate(syn-2.0/clone-impls) >= 2.0.60
Requires:       crate(syn-2.0/derive) >= 2.0.60
Requires:       crate(syn-2.0/extra-traits) >= 2.0.60
Requires:       crate(syn-2.0/full) >= 2.0.60
Requires:       crate(syn-2.0/parsing) >= 2.0.60
Requires:       crate(syn-2.0/printing) >= 2.0.60
Requires:       crate(syn-2.0/visit-mut) >= 2.0.60
Provides:       crate(pyo3-macros-backend) = %{version}
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
