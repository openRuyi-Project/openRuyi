# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rhai
%global full_version 1.26.1
%global pkgname rhai-1

Name:           rust-rhai-1
Version:        1.26.1
Release:        %autorelease
Summary:        Rust crate "rhai"
License:        MIT OR Apache-2.0
URL:            https://rhai.rs
#!RemoteAsset:  sha256:0334639972c0ea5a3fd366aa36116754a11431b619fec3ed559b3f73bcbcebf5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/compile-time-rng) >= 0.8.4
Requires:       crate(bitflags-2) >= 2.3.3
Requires:       crate(num-traits-0.2) >= 0.2.14
Requires:       crate(once-cell-1/alloc) >= 1.20.1
Requires:       crate(once-cell-1/portable-atomic) >= 1.20.1
Requires:       crate(once-cell-1/race) >= 1.20.1
Requires:       crate(rhai-codegen-3/default) >= 3.2.0
Requires:       crate(smallvec-1/const-generics) >= 1.7.0
Requires:       crate(smallvec-1/const-new) >= 1.7.0
Requires:       crate(smallvec-1/union) >= 1.7.0
Requires:       crate(smartstring-1) >= 1.0.0
Requires:       crate(thin-vec-0.2) >= 0.2.13
Requires:       crate(web-time-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debugging) = %{version}
Provides:       crate(%{pkgname}/f32-float) = %{version}
Provides:       crate(%{pkgname}/grain) = %{version}
Provides:       crate(%{pkgname}/internals) = %{version}
Provides:       crate(%{pkgname}/no-closure) = %{version}
Provides:       crate(%{pkgname}/no-custom-syntax) = %{version}
Provides:       crate(%{pkgname}/no-float) = %{version}
Provides:       crate(%{pkgname}/no-function) = %{version}
Provides:       crate(%{pkgname}/no-index) = %{version}
Provides:       crate(%{pkgname}/no-module) = %{version}
Provides:       crate(%{pkgname}/no-object) = %{version}
Provides:       crate(%{pkgname}/no-optimize) = %{version}
Provides:       crate(%{pkgname}/no-position) = %{version}
Provides:       crate(%{pkgname}/no-time) = %{version}
Provides:       crate(%{pkgname}/only-i32) = %{version}
Provides:       crate(%{pkgname}/only-i64) = %{version}
Provides:       crate(%{pkgname}/testing-environ) = %{version}
Provides:       crate(%{pkgname}/unchecked) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "rhai"

%package     -n %{name}+arbitrary
Summary:        Embedded scripting for Rust - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.3.2
Requires:       crate(arbitrary-1/derive) >= 1.3.2
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bin-features
Summary:        Embedded scripting for Rust - feature "bin-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/debugging) = %{version}
Requires:       crate(%{pkgname}/decimal) = %{version}
Requires:       crate(%{pkgname}/metadata) = %{version}
Requires:       crate(%{pkgname}/rustyline) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/bin-features) = %{version}

%description -n %{name}+bin-features
This metapackage enables feature "bin-features" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+core-error
Summary:        Embedded scripting for Rust - feature "core-error"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-error-0.0.0/alloc) >= 0.0.0
Provides:       crate(%{pkgname}/core-error) = %{version}

%description -n %{name}+core-error
This metapackage enables feature "core-error" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Embedded scripting for Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(ahash-0.8/compile-time-rng) >= 0.8.4
Requires:       crate(ahash-0.8/runtime-rng) >= 0.8.4
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Embedded scripting for Rust - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fuzz
Summary:        Embedded scripting for Rust - feature "fuzz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arbitrary) = %{version}
Requires:       crate(%{pkgname}/grain) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(rust-decimal-1/maths) >= 1.24.0
Requires:       crate(rust-decimal-1/rust-fuzz) >= 1.24.0
Provides:       crate(%{pkgname}/fuzz) = %{version}

%description -n %{name}+fuzz
This metapackage enables feature "fuzz" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Embedded scripting for Rust - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3/default) >= 0.3.4
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hashbrown
Summary:        Embedded scripting for Rust - feature "hashbrown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Embedded scripting for Rust - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libm-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+metadata
Summary:        Embedded scripting for Rust - feature "metadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(rhai-codegen-3/metadata) >= 3.2.0
Provides:       crate(%{pkgname}/metadata) = %{version}

%description -n %{name}+metadata
This metapackage enables feature "metadata" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std-compat
Summary:        Embedded scripting for Rust - feature "no-std-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(no-std-compat-0.4/alloc) >= 0.4.1
Provides:       crate(%{pkgname}/no-std-compat) = %{version}

%description -n %{name}+no-std-compat
This metapackage enables feature "no-std-compat" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std
Summary:        Embedded scripting for Rust - feature "no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core-error) = %{version}
Requires:       crate(%{pkgname}/hashbrown) = %{version}
Requires:       crate(%{pkgname}/libm) = %{version}
Requires:       crate(%{pkgname}/no-std-compat) = %{version}
Requires:       crate(%{pkgname}/no-time) = %{version}
Requires:       crate(num-traits-0.2/libm) >= 0.2.14
Provides:       crate(%{pkgname}/no-std) = %{version}

%description -n %{name}+no-std
This metapackage enables feature "no_std" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Embedded scripting for Rust - feature "rust_decimal" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1/maths) >= 1.24.0
Provides:       crate(%{pkgname}/decimal) = %{version}
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "decimal" feature.

%package     -n %{name}+rustyline
Summary:        Embedded scripting for Rust - feature "rustyline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustyline-15/default) >= 15.0.0
Provides:       crate(%{pkgname}/rustyline) = %{version}

%description -n %{name}+rustyline
This metapackage enables feature "rustyline" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Embedded scripting for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.136
Requires:       crate(serde-1/derive) >= 1.0.136
Requires:       crate(smallvec-1/const-generics) >= 1.7.0
Requires:       crate(smallvec-1/const-new) >= 1.7.0
Requires:       crate(smallvec-1/serde) >= 1.7.0
Requires:       crate(smallvec-1/union) >= 1.7.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Embedded scripting for Rust - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/alloc) >= 1.0.45
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Embedded scripting for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.8/compile-time-rng) >= 0.8.4
Requires:       crate(ahash-0.8/std) >= 0.8.4
Requires:       crate(num-traits-0.2/std) >= 0.2.14
Requires:       crate(once-cell-1/alloc) >= 1.20.1
Requires:       crate(once-cell-1/portable-atomic) >= 1.20.1
Requires:       crate(once-cell-1/race) >= 1.20.1
Requires:       crate(once-cell-1/std) >= 1.20.1
Requires:       crate(smartstring-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sync
Summary:        Embedded scripting for Rust - feature "sync"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(no-std-compat-0.4/alloc) >= 0.4.1
Requires:       crate(no-std-compat-0.4/compat-sync) >= 0.4.1
Requires:       crate(rhai-codegen-3/sync) >= 3.2.0
Provides:       crate(%{pkgname}/sync) = %{version}

%description -n %{name}+sync
This metapackage enables feature "sync" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-xid
Summary:        Embedded scripting for Rust - feature "unicode-xid" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-xid-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/unicode-xid) = %{version}
Provides:       crate(%{pkgname}/unicode-xid-ident) = %{version}

%description -n %{name}+unicode-xid
This metapackage enables feature "unicode-xid" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unicode-xid-ident" feature.

%package     -n %{name}+wasm-bindgen
Summary:        Embedded scripting for Rust - feature "wasm-bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.4
Provides:       crate(%{pkgname}/wasm-bindgen) = %{version}

%description -n %{name}+wasm-bindgen
This metapackage enables feature "wasm-bindgen" for the Rust rhai crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
