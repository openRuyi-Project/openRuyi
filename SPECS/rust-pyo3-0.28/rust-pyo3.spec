# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3
%global full_version 0.28.3
%global pkgname pyo3-0.28

Name:           rust-pyo3-0.28
Version:        0.28.3
Release:        %autorelease
Summary:        Rust crate "pyo3"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:91fd8e38a3b50ed1167fb981cd6fd60147e091784c427b8f7183a7ee32c31c12
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.185
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(portable-atomic-1.0/default) >= 1.13.1
Requires:       crate(pyo3-build-config-0.28/default) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/default) >= 0.28.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/auto-initialize)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/py-clone)

%description
Source code for takopackized Rust crate "pyo3"

%package     -n %{name}+abi3
Summary:        Bindings to Python interpreter - feature "abi3"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-build-config-0.28/abi3) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3) >= 0.28.3
Provides:       crate(%{pkgname}/abi3)

%description -n %{name}+abi3
This metapackage enables feature "abi3" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py310
Summary:        Bindings to Python interpreter - feature "abi3-py310"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py311)
Requires:       crate(pyo3-build-config-0.28/abi3-py310) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py310) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py310)

%description -n %{name}+abi3-py310
This metapackage enables feature "abi3-py310" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py311
Summary:        Bindings to Python interpreter - feature "abi3-py311"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py312)
Requires:       crate(pyo3-build-config-0.28/abi3-py311) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py311) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py311)

%description -n %{name}+abi3-py311
This metapackage enables feature "abi3-py311" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py312
Summary:        Bindings to Python interpreter - feature "abi3-py312"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py313)
Requires:       crate(pyo3-build-config-0.28/abi3-py312) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py312) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py312)

%description -n %{name}+abi3-py312
This metapackage enables feature "abi3-py312" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py313
Summary:        Bindings to Python interpreter - feature "abi3-py313"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py314)
Requires:       crate(pyo3-build-config-0.28/abi3-py313) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py313) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py313)

%description -n %{name}+abi3-py313
This metapackage enables feature "abi3-py313" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py314
Summary:        Bindings to Python interpreter - feature "abi3-py314"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3)
Requires:       crate(pyo3-build-config-0.28/abi3-py314) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py314) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py314)

%description -n %{name}+abi3-py314
This metapackage enables feature "abi3-py314" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py37
Summary:        Bindings to Python interpreter - feature "abi3-py37"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py38)
Requires:       crate(pyo3-build-config-0.28/abi3-py37) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py37) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py37)

%description -n %{name}+abi3-py37
This metapackage enables feature "abi3-py37" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py38
Summary:        Bindings to Python interpreter - feature "abi3-py38"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py39)
Requires:       crate(pyo3-build-config-0.28/abi3-py38) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py38) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py38)

%description -n %{name}+abi3-py38
This metapackage enables feature "abi3-py38" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py39
Summary:        Bindings to Python interpreter - feature "abi3-py39"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py310)
Requires:       crate(pyo3-build-config-0.28/abi3-py39) >= 0.28.3
Requires:       crate(pyo3-build-config-0.28/resolve-config) >= 0.28.3
Requires:       crate(pyo3-ffi-0.28/abi3-py39) >= 0.28.3
Provides:       crate(%{pkgname}/abi3-py39)

%description -n %{name}+abi3-py39
This metapackage enables feature "abi3-py39" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+anyhow
Summary:        Bindings to Python interpreter - feature "anyhow"
Requires:       crate(%{pkgname})
Requires:       crate(anyhow-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname}/anyhow)

%description -n %{name}+anyhow
This metapackage enables feature "anyhow" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arc-lock
Summary:        Bindings to Python interpreter - feature "arc_lock"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/lock-api)
Requires:       crate(lock-api-0.4/arc-lock) >= 0.4.0
Requires:       crate(parking-lot-0.12/arc-lock) >= 0.12.0
Provides:       crate(%{pkgname}/arc-lock)

%description -n %{name}+arc-lock
This metapackage enables feature "arc_lock" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal
Summary:        Bindings to Python interpreter - feature "bigdecimal"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/num-bigint)
Requires:       crate(bigdecimal-0.4/default) >= 0.4.7
Provides:       crate(%{pkgname}/bigdecimal)

%description -n %{name}+bigdecimal
This metapackage enables feature "bigdecimal" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Bindings to Python interpreter - feature "bytes"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0/default) >= 1.10
Provides:       crate(%{pkgname}/bytes)

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Bindings to Python interpreter - feature "chrono"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4) >= 0.4.25
Provides:       crate(%{pkgname}/chrono)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-local
Summary:        Bindings to Python interpreter - feature "chrono-local"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4/clock) >= 0.4.25
Requires:       crate(iana-time-zone-0.1/default) >= 0.1.0
Requires:       crate(iana-time-zone-0.1/fallback) >= 0.1.0
Provides:       crate(%{pkgname}/chrono-local)

%description -n %{name}+chrono-local
This metapackage enables feature "chrono-local" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono-tz
Summary:        Bindings to Python interpreter - feature "chrono-tz"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-tz-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/chrono-tz)

%description -n %{name}+chrono-tz
This metapackage enables feature "chrono-tz" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either
Summary:        Bindings to Python interpreter - feature "either"
Requires:       crate(%{pkgname})
Requires:       crate(either-1.0/default) >= 1.9
Provides:       crate(%{pkgname}/either)

%description -n %{name}+either
This metapackage enables feature "either" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-async
Summary:        Bindings to Python interpreter - feature "experimental-async"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/macros)
Requires:       crate(pyo3-macros-0.28/experimental-async) >= 0.28.3
Provides:       crate(%{pkgname}/experimental-async)

%description -n %{name}+experimental-async
This metapackage enables feature "experimental-async" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental-inspect
Summary:        Bindings to Python interpreter - feature "experimental-inspect"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-macros-0.28/experimental-inspect) >= 0.28.3
Provides:       crate(%{pkgname}/experimental-inspect)

%description -n %{name}+experimental-inspect
This metapackage enables feature "experimental-inspect" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extension-module
Summary:        Bindings to Python interpreter - feature "extension-module"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-ffi-0.28/extension-module) >= 0.28.3
Provides:       crate(%{pkgname}/extension-module)

%description -n %{name}+extension-module
This metapackage enables feature "extension-module" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+eyre
Summary:        Bindings to Python interpreter - feature "eyre"
Requires:       crate(%{pkgname})
Requires:       crate(eyre-0.6/default) >= 0.6.8
Provides:       crate(%{pkgname}/eyre)

%description -n %{name}+eyre
This metapackage enables feature "eyre" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Bindings to Python interpreter - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/anyhow)
Requires:       crate(%{pkgname}/arc-lock)
Requires:       crate(%{pkgname}/bigdecimal)
Requires:       crate(%{pkgname}/bytes)
Requires:       crate(%{pkgname}/chrono)
Requires:       crate(%{pkgname}/chrono-local)
Requires:       crate(%{pkgname}/chrono-tz)
Requires:       crate(%{pkgname}/either)
Requires:       crate(%{pkgname}/experimental-async)
Requires:       crate(%{pkgname}/experimental-inspect)
Requires:       crate(%{pkgname}/eyre)
Requires:       crate(%{pkgname}/hashbrown)
Requires:       crate(%{pkgname}/indexmap)
Requires:       crate(%{pkgname}/jiff-02)
Requires:       crate(%{pkgname}/lock-api)
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/num-bigint)
Requires:       crate(%{pkgname}/num-complex)
Requires:       crate(%{pkgname}/num-rational)
Requires:       crate(%{pkgname}/ordered-float)
Requires:       crate(%{pkgname}/parking-lot)
Requires:       crate(%{pkgname}/py-clone)
Requires:       crate(%{pkgname}/rust-decimal)
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/smallvec)
Requires:       crate(%{pkgname}/time)
Requires:       crate(%{pkgname}/uuid)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate-import-lib
Summary:        Bindings to Python interpreter - feature "generate-import-lib"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-ffi-0.28/generate-import-lib) >= 0.28.3
Provides:       crate(%{pkgname}/generate-import-lib)

%description -n %{name}+generate-import-lib
This metapackage enables feature "generate-import-lib" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Bindings to Python interpreter - feature "hashbrown"
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.15) >= 0.15.0
Provides:       crate(%{pkgname}/hashbrown)

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Bindings to Python interpreter - feature "indexmap"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname}/indexmap)

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inventory
Summary:        Bindings to Python interpreter - feature "inventory"
Requires:       crate(%{pkgname})
Requires:       crate(inventory-0.3/default) >= 0.3.5
Provides:       crate(%{pkgname}/inventory)

%description -n %{name}+inventory
This metapackage enables feature "inventory" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff-02
Summary:        Bindings to Python interpreter - feature "jiff-02"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/jiff-02)

%description -n %{name}+jiff-02
This metapackage enables feature "jiff-02" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lock-api
Summary:        Bindings to Python interpreter - feature "lock_api"
Requires:       crate(%{pkgname})
Requires:       crate(lock-api-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/lock-api)

%description -n %{name}+lock-api
This metapackage enables feature "lock_api" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+multiple-pymethods
Summary:        Bindings to Python interpreter - feature "multiple-pymethods"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/inventory)
Requires:       crate(pyo3-macros-0.28/multiple-pymethods) >= 0.28.3
Provides:       crate(%{pkgname}/multiple-pymethods)

%description -n %{name}+multiple-pymethods
This metapackage enables feature "multiple-pymethods" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Bindings to Python interpreter - feature "num-bigint"
Requires:       crate(%{pkgname})
Requires:       crate(num-bigint-0.4/default) >= 0.4.6
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Provides:       crate(%{pkgname}/num-bigint)

%description -n %{name}+num-bigint
This metapackage enables feature "num-bigint" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-complex
Summary:        Bindings to Python interpreter - feature "num-complex"
Requires:       crate(%{pkgname})
Requires:       crate(num-complex-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/num-complex)

%description -n %{name}+num-complex
This metapackage enables feature "num-complex" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-rational
Summary:        Bindings to Python interpreter - feature "num-rational"
Requires:       crate(%{pkgname})
Requires:       crate(num-rational-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/num-rational)

%description -n %{name}+num-rational
This metapackage enables feature "num-rational" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ordered-float
Summary:        Bindings to Python interpreter - feature "ordered-float"
Requires:       crate(%{pkgname})
Requires:       crate(ordered-float-5.0) >= 5.0.0
Provides:       crate(%{pkgname}/ordered-float)

%description -n %{name}+ordered-float
This metapackage enables feature "ordered-float" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking-lot
Summary:        Bindings to Python interpreter - feature "parking_lot"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/lock-api)
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/parking-lot)

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pyo3-macros
Summary:        Bindings to Python interpreter - feature "pyo3-macros" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-macros-0.28/default) >= 0.28.3
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/macros)
Provides:       crate(%{pkgname}/pyo3-macros)

%description -n %{name}+pyo3-macros
This metapackage enables feature "pyo3-macros" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "macros" features.

%package     -n %{name}+rust-decimal
Summary:        Bindings to Python interpreter - feature "rust_decimal"
Requires:       crate(%{pkgname})
Requires:       crate(rust-decimal-1.0) >= 1.15
Provides:       crate(%{pkgname}/rust-decimal)

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Bindings to Python interpreter - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Bindings to Python interpreter - feature "smallvec"
Requires:       crate(%{pkgname})
Requires:       crate(smallvec-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec)

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Bindings to Python interpreter - feature "time"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3) >= 0.3.38
Provides:       crate(%{pkgname}/time)

%description -n %{name}+time
This metapackage enables feature "time" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Bindings to Python interpreter - feature "uuid"
Requires:       crate(%{pkgname})
Requires:       crate(uuid-1.0/default) >= 1.12.0
Provides:       crate(%{pkgname}/uuid)

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
