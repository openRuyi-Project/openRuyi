# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3
%global full_version 0.26.0
%global pkgname pyo3-0.26

Name:           rust-pyo3-0.26
Version:        0.26.0
Release:        %autorelease
Summary:        Rust crate "pyo3"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:7ba0117f4212101ee6544044dae45abe1083d30ce7b29c4b5cbdfa2354e07383
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.62
Requires:       crate(memoffset-0.9/default) >= 0.9.0
Requires:       crate(once-cell-1/default) >= 1.21.0
Requires:       crate(portable-atomic-1/default) >= 1.0.0
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/auto-initialize) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/py-clone) = %{version}

%description
Source code for takopackized Rust crate "pyo3"

%package     -n %{name}+abi3
Summary:        Bindings to Python interpreter - feature "abi3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3) >= 0.26.0
Provides:       crate(%{pkgname}/abi3) = %{version}

%description -n %{name}+abi3
This metapackage enables feature "abi3" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py310
Summary:        Bindings to Python interpreter - feature "abi3-py310"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py311) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py310) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py310) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py310) = %{version}

%description -n %{name}+abi3-py310
This metapackage enables feature "abi3-py310" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py311
Summary:        Bindings to Python interpreter - feature "abi3-py311"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py312) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py311) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py311) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py311) = %{version}

%description -n %{name}+abi3-py311
This metapackage enables feature "abi3-py311" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py312
Summary:        Bindings to Python interpreter - feature "abi3-py312"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py313) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py312) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py312) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py312) = %{version}

%description -n %{name}+abi3-py312
This metapackage enables feature "abi3-py312" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py313
Summary:        Bindings to Python interpreter - feature "abi3-py313"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py314) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py313) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py313) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py313) = %{version}

%description -n %{name}+abi3-py313
This metapackage enables feature "abi3-py313" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py314
Summary:        Bindings to Python interpreter - feature "abi3-py314"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py314) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py314) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py314) = %{version}

%description -n %{name}+abi3-py314
This metapackage enables feature "abi3-py314" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py37
Summary:        Bindings to Python interpreter - feature "abi3-py37"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py38) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py37) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py37) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py37) = %{version}

%description -n %{name}+abi3-py37
This metapackage enables feature "abi3-py37" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py38
Summary:        Bindings to Python interpreter - feature "abi3-py38"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py39) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py38) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py38) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py38) = %{version}

%description -n %{name}+abi3-py38
This metapackage enables feature "abi3-py38" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py39
Summary:        Bindings to Python interpreter - feature "abi3-py39"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/abi3-py310) = %{version}
Requires:       crate(pyo3-build-config-0.26) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/abi3-py39) >= 0.26.0
Requires:       crate(pyo3-build-config-0.26/resolve-config) >= 0.26.0
Requires:       crate(pyo3-ffi-0.26/abi3-py39) >= 0.26.0
Provides:       crate(%{pkgname}/abi3-py39) = %{version}

%description -n %{name}+abi3-py39
This metapackage enables feature "abi3-py39" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+anyhow
Summary:        Bindings to Python interpreter - feature "anyhow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anyhow-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/anyhow) = %{version}

%description -n %{name}+anyhow
This metapackage enables feature "anyhow" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arc-lock
Summary:        Bindings to Python interpreter - feature "arc_lock"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lock-api) = %{version}
Requires:       crate(lock-api-0.4/arc-lock) >= 0.4.0
Requires:       crate(parking-lot-0.12/arc-lock) >= 0.12.0
Provides:       crate(%{pkgname}/arc-lock) = %{version}

%description -n %{name}+arc-lock
This metapackage enables feature "arc_lock" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        Bindings to Python interpreter - feature "bigdecimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-bigint) = %{version}
Requires:       crate(bigdecimal-0.4/default) >= 0.4.7
Provides:       crate(%{pkgname}/bigdecimal) = %{version}

%description -n %{name}+bigdecimal
This metapackage enables feature "bigdecimal" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Bindings to Python interpreter - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Bindings to Python interpreter - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4) >= 0.4.25
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-local
Summary:        Bindings to Python interpreter - feature "chrono-local"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/clock) >= 0.4.25
Requires:       crate(iana-time-zone-0.1/default) >= 0.1.0
Requires:       crate(iana-time-zone-0.1/fallback) >= 0.1.0
Provides:       crate(%{pkgname}/chrono-local) = %{version}

%description -n %{name}+chrono-local
This metapackage enables feature "chrono-local" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-tz
Summary:        Bindings to Python interpreter - feature "chrono-tz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-tz-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/chrono-tz) = %{version}

%description -n %{name}+chrono-tz
This metapackage enables feature "chrono-tz" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either
Summary:        Bindings to Python interpreter - feature "either"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/either) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-async
Summary:        Bindings to Python interpreter - feature "experimental-async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(pyo3-macros-0.26/experimental-async) >= 0.26.0
Provides:       crate(%{pkgname}/experimental-async) = %{version}

%description -n %{name}+experimental-async
This metapackage enables feature "experimental-async" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-inspect
Summary:        Bindings to Python interpreter - feature "experimental-inspect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-macros-0.26/experimental-inspect) >= 0.26.0
Provides:       crate(%{pkgname}/experimental-inspect) = %{version}

%description -n %{name}+experimental-inspect
This metapackage enables feature "experimental-inspect" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extension-module
Summary:        Bindings to Python interpreter - feature "extension-module"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-ffi-0.26/extension-module) >= 0.26.0
Provides:       crate(%{pkgname}/extension-module) = %{version}

%description -n %{name}+extension-module
This metapackage enables feature "extension-module" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+eyre
Summary:        Bindings to Python interpreter - feature "eyre"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(eyre-0.6/default) >= 0.6.8
Provides:       crate(%{pkgname}/eyre) = %{version}

%description -n %{name}+eyre
This metapackage enables feature "eyre" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Bindings to Python interpreter - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/anyhow) = %{version}
Requires:       crate(%{pkgname}/arc-lock) = %{version}
Requires:       crate(%{pkgname}/bigdecimal) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/chrono-local) = %{version}
Requires:       crate(%{pkgname}/chrono-tz) = %{version}
Requires:       crate(%{pkgname}/either) = %{version}
Requires:       crate(%{pkgname}/experimental-async) = %{version}
Requires:       crate(%{pkgname}/experimental-inspect) = %{version}
Requires:       crate(%{pkgname}/eyre) = %{version}
Requires:       crate(%{pkgname}/hashbrown) = %{version}
Requires:       crate(%{pkgname}/indexmap) = %{version}
Requires:       crate(%{pkgname}/jiff-02) = %{version}
Requires:       crate(%{pkgname}/lock-api) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/num-bigint) = %{version}
Requires:       crate(%{pkgname}/num-complex) = %{version}
Requires:       crate(%{pkgname}/num-rational) = %{version}
Requires:       crate(%{pkgname}/ordered-float) = %{version}
Requires:       crate(%{pkgname}/parking-lot) = %{version}
Requires:       crate(%{pkgname}/py-clone) = %{version}
Requires:       crate(%{pkgname}/rust-decimal) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/smallvec) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Requires:       crate(%{pkgname}/uuid) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate-import-lib
Summary:        Bindings to Python interpreter - feature "generate-import-lib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-ffi-0.26/generate-import-lib) >= 0.26.0
Provides:       crate(%{pkgname}/generate-import-lib) = %{version}

%description -n %{name}+generate-import-lib
This metapackage enables feature "generate-import-lib" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Bindings to Python interpreter - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Bindings to Python interpreter - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.5.0
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indoc
Summary:        Bindings to Python interpreter - feature "indoc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indoc-2/default) >= 2.0.1
Provides:       crate(%{pkgname}/indoc) = %{version}

%description -n %{name}+indoc
This metapackage enables feature "indoc" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inventory
Summary:        Bindings to Python interpreter - feature "inventory"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(inventory-0.3/default) >= 0.3.5
Provides:       crate(%{pkgname}/inventory) = %{version}

%description -n %{name}+inventory
This metapackage enables feature "inventory" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff-02
Summary:        Bindings to Python interpreter - feature "jiff-02"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/jiff-02) = %{version}

%description -n %{name}+jiff-02
This metapackage enables feature "jiff-02" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lock-api
Summary:        Bindings to Python interpreter - feature "lock_api"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lock-api-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/lock-api) = %{version}

%description -n %{name}+lock-api
This metapackage enables feature "lock_api" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Bindings to Python interpreter - feature "macros" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/indoc) = %{version}
Requires:       crate(%{pkgname}/pyo3-macros) = %{version}
Requires:       crate(%{pkgname}/unindent) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+multiple-pymethods
Summary:        Bindings to Python interpreter - feature "multiple-pymethods"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/inventory) = %{version}
Requires:       crate(pyo3-macros-0.26/multiple-pymethods) >= 0.26.0
Provides:       crate(%{pkgname}/multiple-pymethods) = %{version}

%description -n %{name}+multiple-pymethods
This metapackage enables feature "multiple-pymethods" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Bindings to Python interpreter - feature "num-bigint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-bigint-0.4/default) >= 0.4.2
Provides:       crate(%{pkgname}/num-bigint) = %{version}

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-complex
Summary:        Bindings to Python interpreter - feature "num-complex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-complex-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/num-complex) = %{version}

%description -n %{name}+num-complex
This metapackage enables feature "num-complex" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-rational
Summary:        Bindings to Python interpreter - feature "num-rational"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-rational-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/num-rational) = %{version}

%description -n %{name}+num-rational
This metapackage enables feature "num-rational" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ordered-float
Summary:        Bindings to Python interpreter - feature "ordered-float"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ordered-float-5) >= 5.0.0
Provides:       crate(%{pkgname}/ordered-float) = %{version}

%description -n %{name}+ordered-float
This metapackage enables feature "ordered-float" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Bindings to Python interpreter - feature "parking_lot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lock-api) = %{version}
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/parking-lot) = %{version}

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pyo3-macros
Summary:        Bindings to Python interpreter - feature "pyo3-macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-macros-0.26/default) >= 0.26.0
Provides:       crate(%{pkgname}/pyo3-macros) = %{version}

%description -n %{name}+pyo3-macros
This metapackage enables feature "pyo3-macros" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Bindings to Python interpreter - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1) >= 1.15.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Bindings to Python interpreter - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Bindings to Python interpreter - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Bindings to Python interpreter - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3) >= 0.3.38
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unindent
Summary:        Bindings to Python interpreter - feature "unindent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unindent-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/unindent) = %{version}

%description -n %{name}+unindent
This metapackage enables feature "unindent" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Bindings to Python interpreter - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
