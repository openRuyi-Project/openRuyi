# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros
%global full_version 0.23.5
%global pkgname pyo3-macros-0.23

Name:           rust-pyo3-macros-0.23
Version:        0.23.5
Release:        %autorelease
Summary:        Rust crate "pyo3-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:fbc2201328f63c4710f68abdf653c89d8dbc2858b88c5d88b0ff38a75288a9da
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.60
Requires:       crate(pyo3-macros-backend-0.23/default) >= 0.23.5
Requires:       crate(quote-1.0/default) >= 1.0.0
Requires:       crate(syn-2.0/default) >= 2.0.0
Requires:       crate(syn-2.0/extra-traits) >= 2.0.0
Requires:       crate(syn-2.0/full) >= 2.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/multiple-pymethods)

%description
Source code for takopackized Rust crate "pyo3-macros"

%package     -n %{name}+experimental-async
Summary:        Proc macros for PyO3 package - feature "experimental-async"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-macros-backend-0.23/experimental-async) >= 0.23.5
Provides:       crate(%{pkgname}/experimental-async)

%description -n %{name}+experimental-async
This metapackage enables feature "experimental-async" for the Rust pyo3-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
