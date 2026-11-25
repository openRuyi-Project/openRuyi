# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name noyalib
%global full_version 0.0.5
%global pkgname noyalib-0.0.5

Name:           rust-noyalib-0.0.5
Version:        0.0.5
Release:        %autorelease
Summary:        Rust crate "noyalib"
License:        MIT OR Apache-2.0
URL:            https://github.com/sebastienrousseau/noyalib
#!RemoteAsset:  sha256:e493c05128df7a83b9676b709d590e0ebc285c7ed3152bc679668e8c1e506af5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(indexmap-2/serde) >= 2.0.0
Requires:       crate(memchr-2/default) >= 2.7.0
Requires:       crate(rustc-hash-2/default) >= 2.0.0
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(smallvec-1) >= 1.13.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compat-serde-yaml) = %{version}
Provides:       crate(%{pkgname}/include) = %{version}
Provides:       crate(%{pkgname}/nightly-simd) = %{version}
Provides:       crate(%{pkgname}/robotics) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}
Provides:       crate(%{pkgname}/wasm-opt) = %{version}

%description
Source code for takopackized Rust crate "noyalib"

%package     -n %{name}+ariadne
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "ariadne"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ariadne-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/ariadne) = %{version}

%description -n %{name}+ariadne
This metapackage enables feature "ariadne" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compare-saphyr
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "compare-saphyr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-saphyr-0.0.0/default) >= 0.0.0
Provides:       crate(%{pkgname}/compare-saphyr) = %{version}

%description -n %{name}+compare-saphyr
This metapackage enables feature "compare-saphyr" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fast-float) = %{version}
Requires:       crate(%{pkgname}/fast-int) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/strict-deserialise) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast-float
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "fast-float"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ryu-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/fast-float) = %{version}

%description -n %{name}+fast-float
This metapackage enables feature "fast-float" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fast-int
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "fast-int"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(itoa-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/fast-int) = %{version}

%description -n %{name}+fast-int
This metapackage enables feature "fast-int" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+figment
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "figment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(figment-0.10/default) >= 0.10.0
Requires:       crate(figment-0.10/env) >= 0.10.0
Provides:       crate(%{pkgname}/figment) = %{version}

%description -n %{name}+figment
This metapackage enables feature "figment" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+garde
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "garde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(garde-0.22/derive) >= 0.22.0
Provides:       crate(%{pkgname}/garde) = %{version}

%description -n %{name}+garde
This metapackage enables feature "garde" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+include-fs
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "include_fs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/include) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/include-fs) = %{version}

%description -n %{name}+include-fs
This metapackage enables feature "include_fs" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+miette
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "miette"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(miette-7/default) >= 7.0.0
Provides:       crate(%{pkgname}/miette) = %{version}

%description -n %{name}+miette
This metapackage enables feature "miette" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+noyavalidate
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "noyavalidate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/miette) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/validate-schema) = %{version}
Requires:       crate(miette-7/fancy) >= 7.0.0
Provides:       crate(%{pkgname}/noyavalidate) = %{version}

%description -n %{name}+noyavalidate
This metapackage enables feature "noyavalidate" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(rayon-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schema
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "schema"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-1/derive) >= 1.2.0
Requires:       crate(schemars-1/std) >= 1.2.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/schema) = %{version}

%description -n %{name}+schema
This metapackage enables feature "schema" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/minimal) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "minimal" feature.

%package     -n %{name}+strict-deserialise
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "strict-deserialise"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-ignored-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/strict-deserialise) = %{version}

%description -n %{name}+strict-deserialise
This metapackage enables feature "strict-deserialise" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+validate-schema
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "validate-schema"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/schema) = %{version}
Requires:       crate(jsonschema-0.33) >= 0.33.0
Provides:       crate(%{pkgname}/validate-schema) = %{version}

%description -n %{name}+validate-schema
This metapackage enables feature "validate-schema" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+validator
Summary:        Pure Rust YAML library with zero unsafe code and full serde integration - feature "validator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(validator-0.19/default) >= 0.19.0
Requires:       crate(validator-0.19/derive) >= 0.19.0
Provides:       crate(%{pkgname}/validator) = %{version}

%description -n %{name}+validator
This metapackage enables feature "validator" for the Rust noyalib crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
