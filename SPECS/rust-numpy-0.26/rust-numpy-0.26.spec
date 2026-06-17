# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name numpy
%global full_version 0.26.0
%global pkgname numpy-0.26

Name:           rust-numpy-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "numpy"
License:        BSD-2-Clause
URL:            https://github.com/PyO3/rust-numpy
#!RemoteAsset:  sha256:9b2dba356160b54f5371b550575b78130a54718b4c6e46b3f33a6da74a27e78b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(ndarray-0.15/default) >= 0.15.0
Requires:       crate(num-complex-0.2/default) >= 0.2.0
Requires:       crate(num-integer-0.1/default) >= 0.1.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(pyo3-0.26/macros) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(rustc-hash-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "numpy"

%package     -n %{name}+half
Summary:        PyO3-based Rust bindings of the NumPy C-API - feature "half"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(half-2) >= 2.0.0
Provides:       crate(%{pkgname}/half) = %{version}

%description -n %{name}+half
This metapackage enables feature "half" for the Rust numpy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nalgebra
Summary:        PyO3-based Rust bindings of the NumPy C-API - feature "nalgebra"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nalgebra-0.30) >= 0.30.0
Provides:       crate(%{pkgname}/nalgebra) = %{version}

%description -n %{name}+nalgebra
This metapackage enables feature "nalgebra" for the Rust numpy crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
