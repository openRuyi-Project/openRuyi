# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3-ffi
%global full_version 0.23.5
%global pkgname pyo3-ffi-0.23

Name:           rust-pyo3-ffi-0.23
Version:        0.23.5
Release:        %autorelease
Summary:        Rust crate "pyo3-ffi"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:e9f1b4c431c0bb1c8fb0a338709859eed0d030ff6daa34368d3b152a63dfdd8d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.62
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pyo3-ffi"

%package     -n %{name}+abi3
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/abi3) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/abi3) = %{version}

%description -n %{name}+abi3
This metapackage enables feature "abi3" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py310
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py310"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py311) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/abi3-py310) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py310) = %{version}

%description -n %{name}+abi3-py310
This metapackage enables feature "abi3-py310" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py311
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py311"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py312) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/abi3-py311) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py311) = %{version}

%description -n %{name}+abi3-py311
This metapackage enables feature "abi3-py311" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py312
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py312"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/abi3-py312) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py312) = %{version}

%description -n %{name}+abi3-py312
This metapackage enables feature "abi3-py312" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py37
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py37"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py38) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/abi3-py37) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py37) = %{version}

%description -n %{name}+abi3-py37
This metapackage enables feature "abi3-py37" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py38
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py38"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py39) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/abi3-py38) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py38) = %{version}

%description -n %{name}+abi3-py38
This metapackage enables feature "abi3-py38" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py39
Summary:        Python-API bindings for the PyO3 ecosystem - feature "abi3-py39"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py310) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/abi3-py39) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py39) = %{version}

%description -n %{name}+abi3-py39
This metapackage enables feature "abi3-py39" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extension-module
Summary:        Python-API bindings for the PyO3 ecosystem - feature "extension-module"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/extension-module) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/extension-module) = %{version}

%description -n %{name}+extension-module
This metapackage enables feature "extension-module" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate-import-lib
Summary:        Python-API bindings for the PyO3 ecosystem - feature "generate-import-lib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-build-config-0.23) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/python3-dll-a) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Provides:       crate(%{pkgname}/generate-import-lib) = %{version}

%description -n %{name}+generate-import-lib
This metapackage enables feature "generate-import-lib" for the Rust pyo3-ffi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
