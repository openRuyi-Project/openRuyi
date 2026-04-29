# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros
%global full_version 0.28.3
%global pkgname pyo3-macros-0.28

Name:           rust-pyo3-macros-0.28
Version:        0.28.3
Release:        %autorelease
Summary:        Rust crate "pyo3-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:df6e520eff47c45997d2fc7dd8214b25dd1310918bbb2642156ef66a67f29813
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(pyo3-macros-backend-0.28/default) >= 0.28.3
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/multiple-pymethods)

%description
Source code for takopackized Rust crate "pyo3-macros"

%package     -n %{name}+experimental-async
Summary:        Proc macros for PyO3 package - feature "experimental-async"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-macros-backend-0.28/experimental-async) >= 0.28.3
Provides:       crate(%{pkgname}/experimental-async)

%description -n %{name}+experimental-async
This metapackage enables feature "experimental-async" for the Rust pyo3-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-inspect
Summary:        Proc macros for PyO3 package - feature "experimental-inspect"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-macros-backend-0.28/experimental-inspect) >= 0.28.3
Provides:       crate(%{pkgname}/experimental-inspect)

%description -n %{name}+experimental-inspect
This metapackage enables feature "experimental-inspect" for the Rust pyo3-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
