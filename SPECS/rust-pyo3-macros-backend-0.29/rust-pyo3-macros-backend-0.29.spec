# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros-backend
%global full_version 0.29.0
%global pkgname pyo3-macros-backend-0.29

Name:           rust-pyo3-macros-backend-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "pyo3-macros-backend"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:4ca3a1557399783172dc5bf39cfca835157732532cba56b71d2292161e53b362
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1) >= 1.0.60
Requires:       crate(quote-1) >= 1.0.37
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
