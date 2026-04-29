# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pyo3
%global full_version 0.23.5
%global pkgname pyo3-0.23

Name:           rust-pyo3-0.23
Version:        0.23.5
Release:        %autorelease
Summary:        Rust crate "pyo3"
License:        MIT OR Apache-2.0
URL:            https://github.com/pyo3/pyo3
#!RemoteAsset:  sha256:7778bffd85cf38175ac1f545509665d0b9b92a198ca7941f131f85f7a4f9a872
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.62
Requires:       crate(memoffset-0.9/default) >= 0.9.0
Requires:       crate(once-cell-1.0/default) >= 1.13
Requires:       crate(portable-atomic-1.0/default) >= 1.0.0
Requires:       crate(pyo3-build-config-0.23/default) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/default) >= 0.23.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/auto-initialize)
Provides:       crate(%{pkgname}/experimental-inspect)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/py-clone)

%description
Source code for takopackized Rust crate "pyo3"

%package     -n %{name}+abi3
Summary:        Bindings to Python interpreter - feature "abi3"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-build-config-0.23/abi3) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/abi3) >= 0.23.5
Provides:       crate(%{pkgname}/abi3)

%description -n %{name}+abi3
This metapackage enables feature "abi3" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py310
Summary:        Bindings to Python interpreter - feature "abi3-py310"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py311)
Requires:       crate(pyo3-build-config-0.23/abi3-py310) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/abi3-py310) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py310)

%description -n %{name}+abi3-py310
This metapackage enables feature "abi3-py310" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py311
Summary:        Bindings to Python interpreter - feature "abi3-py311"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py312)
Requires:       crate(pyo3-build-config-0.23/abi3-py311) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/abi3-py311) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py311)

%description -n %{name}+abi3-py311
This metapackage enables feature "abi3-py311" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py312
Summary:        Bindings to Python interpreter - feature "abi3-py312"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3)
Requires:       crate(pyo3-build-config-0.23/abi3-py312) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/abi3-py312) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py312)

%description -n %{name}+abi3-py312
This metapackage enables feature "abi3-py312" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py37
Summary:        Bindings to Python interpreter - feature "abi3-py37"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py38)
Requires:       crate(pyo3-build-config-0.23/abi3-py37) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/abi3-py37) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py37)

%description -n %{name}+abi3-py37
This metapackage enables feature "abi3-py37" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py38
Summary:        Bindings to Python interpreter - feature "abi3-py38"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py39)
Requires:       crate(pyo3-build-config-0.23/abi3-py38) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/abi3-py38) >= 0.23.5
Provides:       crate(%{pkgname}/abi3-py38)

%description -n %{name}+abi3-py38
This metapackage enables feature "abi3-py38" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+abi3-py39
Summary:        Bindings to Python interpreter - feature "abi3-py39"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/abi3-py310)
Requires:       crate(pyo3-build-config-0.23/abi3-py39) >= 0.23.5
Requires:       crate(pyo3-build-config-0.23/resolve-config) >= 0.23.5
Requires:       crate(pyo3-ffi-0.23/abi3-py39) >= 0.23.5
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

%package     -n %{name}+chrono
Summary:        Bindings to Python interpreter - feature "chrono"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4) >= 0.4.25
Provides:       crate(%{pkgname}/chrono)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

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
Requires:       crate(pyo3-macros-0.23/experimental-async) >= 0.23.5
Provides:       crate(%{pkgname}/experimental-async)

%description -n %{name}+experimental-async
This metapackage enables feature "experimental-async" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extension-module
Summary:        Bindings to Python interpreter - feature "extension-module"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-ffi-0.23/extension-module) >= 0.23.5
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
Requires:       crate(%{pkgname}/chrono)
Requires:       crate(%{pkgname}/chrono-tz)
Requires:       crate(%{pkgname}/either)
Requires:       crate(%{pkgname}/experimental-async)
Requires:       crate(%{pkgname}/experimental-inspect)
Requires:       crate(%{pkgname}/eyre)
Requires:       crate(%{pkgname}/hashbrown)
Requires:       crate(%{pkgname}/indexmap)
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/num-bigint)
Requires:       crate(%{pkgname}/num-complex)
Requires:       crate(%{pkgname}/num-rational)
Requires:       crate(%{pkgname}/py-clone)
Requires:       crate(%{pkgname}/rust-decimal)
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/smallvec)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+generate-import-lib
Summary:        Bindings to Python interpreter - feature "generate-import-lib"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-ffi-0.23/generate-import-lib) >= 0.23.5
Provides:       crate(%{pkgname}/generate-import-lib)

%description -n %{name}+generate-import-lib
This metapackage enables feature "generate-import-lib" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Bindings to Python interpreter - feature "hashbrown"
Requires:       crate(%{pkgname})
Requires:       crate(hashbrown-0.14/default) >= 0.14.5
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

%package     -n %{name}+indoc
Summary:        Bindings to Python interpreter - feature "indoc"
Requires:       crate(%{pkgname})
Requires:       crate(indoc-2.0/default) >= 2.0.1
Provides:       crate(%{pkgname}/indoc)

%description -n %{name}+indoc
This metapackage enables feature "indoc" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inventory
Summary:        Bindings to Python interpreter - feature "inventory"
Requires:       crate(%{pkgname})
Requires:       crate(inventory-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/inventory)

%description -n %{name}+inventory
This metapackage enables feature "inventory" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Bindings to Python interpreter - feature "macros" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/indoc)
Requires:       crate(%{pkgname}/pyo3-macros)
Requires:       crate(%{pkgname}/unindent)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+multiple-pymethods
Summary:        Bindings to Python interpreter - feature "multiple-pymethods"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/inventory)
Requires:       crate(pyo3-macros-0.23/multiple-pymethods) >= 0.23.5
Provides:       crate(%{pkgname}/multiple-pymethods)

%description -n %{name}+multiple-pymethods
This metapackage enables feature "multiple-pymethods" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+num-bigint
Summary:        Bindings to Python interpreter - feature "num-bigint"
Requires:       crate(%{pkgname})
Requires:       crate(num-bigint-0.4/default) >= 0.4.2
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

%package     -n %{name}+pyo3-macros
Summary:        Bindings to Python interpreter - feature "pyo3-macros"
Requires:       crate(%{pkgname})
Requires:       crate(pyo3-macros-0.23/default) >= 0.23.5
Provides:       crate(%{pkgname}/pyo3-macros)

%description -n %{name}+pyo3-macros
This metapackage enables feature "pyo3-macros" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

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

%package     -n %{name}+unindent
Summary:        Bindings to Python interpreter - feature "unindent"
Requires:       crate(%{pkgname})
Requires:       crate(unindent-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/unindent)

%description -n %{name}+unindent
This metapackage enables feature "unindent" for the Rust pyo3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
