# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-macros
%global full_version 0.29.0
%global pkgname pyo3-macros-0.29

Name:           rust-pyo3-macros-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "pyo3-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:9ac53762fd065daa3194dd09337a38bd793a188100fd1a9304c4ab312d901771
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.60
Requires:       crate(pyo3-macros-backend-0.29/default) >= 0.29.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/multiple-pymethods) = %{version}

%description
Source code for takopackized Rust crate "pyo3-macros"

%package     -n %{name}+experimental-async
Summary:        Proc macros for PyO3 package - feature "experimental-async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-macros-backend-0.29/experimental-async) >= 0.29.0
Provides:       crate(%{pkgname}/experimental-async) = %{version}

%description -n %{name}+experimental-async
This metapackage enables feature "experimental-async" for the Rust pyo3-macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-inspect
Summary:        Proc macros for PyO3 package - feature "experimental-inspect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-macros-backend-0.29/experimental-inspect) >= 0.29.0
Provides:       crate(%{pkgname}/experimental-inspect) = %{version}

%description -n %{name}+experimental-inspect
This metapackage enables feature "experimental-inspect" for the Rust pyo3-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
