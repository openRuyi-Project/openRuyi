# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-ffi
%global full_version 0.29.0
%global pkgname pyo3-ffi-0.29

Name:           rust-pyo3-ffi-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "pyo3-ffi"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:ca85c467da1bbc8d866eea5deff9cf29ea5f7785054a17da36e65bda9c05845b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.62
Requires:       crate(pyo3-build-config-0.29) >= 0.29.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/abi3) = %{version}
Provides:       crate(%{pkgname}/abi3-py310) = %{version}
Provides:       crate(%{pkgname}/abi3-py311) = %{version}
Provides:       crate(%{pkgname}/abi3-py312) = %{version}
Provides:       crate(%{pkgname}/abi3-py313) = %{version}
Provides:       crate(%{pkgname}/abi3-py314) = %{version}
Provides:       crate(%{pkgname}/abi3-py315) = %{version}
Provides:       crate(%{pkgname}/abi3-py38) = %{version}
Provides:       crate(%{pkgname}/abi3-py39) = %{version}
Provides:       crate(%{pkgname}/abi3t) = %{version}
Provides:       crate(%{pkgname}/abi3t-py315) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pyo3-ffi"

%package     -n %{name}+extension-module
Summary:        Python-API bindings for the PyO3 ecosystem - feature "extension-module"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-build-config-0.29) >= 0.29.0
Requires:       crate(pyo3-build-config-0.29/extension-module) >= 0.29.0
Provides:       crate(%{pkgname}/extension-module) = %{version}

%description -n %{name}+extension-module
This metapackage enables feature "extension-module" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate-import-lib
Summary:        Python-API bindings for the PyO3 ecosystem - feature "generate-import-lib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-build-config-0.29) >= 0.29.0
Requires:       crate(pyo3-build-config-0.29/generate-import-lib) >= 0.29.0
Provides:       crate(%{pkgname}/generate-import-lib) = %{version}

%description -n %{name}+generate-import-lib
This metapackage enables feature "generate-import-lib" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
