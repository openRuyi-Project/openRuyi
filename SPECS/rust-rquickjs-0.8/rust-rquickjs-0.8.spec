# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rquickjs
%global full_version 0.8.1
%global pkgname rquickjs-0.8

Name:           rust-rquickjs-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "rquickjs"
License:        MIT
URL:            https://github.com/DelSkayn/rquickjs.git
#!RemoteAsset:  sha256:d16661bff09e9ed8e01094a188b463de45ec0693ade55b92ed54027d7ba7c40c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rquickjs-core-0.8/default) >= 0.8.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rquickjs"

%package     -n %{name}+allocator
Summary:        High level bindings to the QuickJS JavaScript engine - feature "allocator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/allocator) >= 0.8.1
Provides:       crate(%{pkgname}/allocator) = %{version}

%description -n %{name}+allocator
This metapackage enables feature "allocator" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+array-buffer
Summary:        High level bindings to the QuickJS JavaScript engine - feature "array-buffer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/array-buffer) >= 0.8.1
Provides:       crate(%{pkgname}/array-buffer) = %{version}

%description -n %{name}+array-buffer
This metapackage enables feature "array-buffer" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bindgen
Summary:        High level bindings to the QuickJS JavaScript engine - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/bindgen) >= 0.8.1
Requires:       crate(rquickjs-macro-0.8/bindgen) >= 0.8.1
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        High level bindings to the QuickJS JavaScript engine - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/chrono) >= 0.8.1
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+classes
Summary:        High level bindings to the QuickJS JavaScript engine - feature "classes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/classes) >= 0.8.1
Provides:       crate(%{pkgname}/classes) = %{version}

%description -n %{name}+classes
This metapackage enables feature "classes" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compile-tests
Summary:        High level bindings to the QuickJS JavaScript engine - feature "compile-tests"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/compile-tests) >= 0.8.1
Provides:       crate(%{pkgname}/compile-tests) = %{version}

%description -n %{name}+compile-tests
This metapackage enables feature "compile-tests" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        High level bindings to the QuickJS JavaScript engine - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/classes) = %{version}
Requires:       crate(%{pkgname}/properties) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+doc-cfg
Summary:        High level bindings to the QuickJS JavaScript engine - feature "doc-cfg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/doc-cfg) >= 0.8.1
Provides:       crate(%{pkgname}/doc-cfg) = %{version}

%description -n %{name}+doc-cfg
This metapackage enables feature "doc-cfg" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-atoms
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-atoms"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-atoms) >= 0.8.1
Provides:       crate(%{pkgname}/dump-atoms) = %{version}

%description -n %{name}+dump-atoms
This metapackage enables feature "dump-atoms" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-bytecode
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-bytecode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-bytecode) >= 0.8.1
Provides:       crate(%{pkgname}/dump-bytecode) = %{version}

%description -n %{name}+dump-bytecode
This metapackage enables feature "dump-bytecode" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-free
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-free"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-free) >= 0.8.1
Provides:       crate(%{pkgname}/dump-free) = %{version}

%description -n %{name}+dump-free
This metapackage enables feature "dump-free" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-gc
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-gc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-gc) >= 0.8.1
Provides:       crate(%{pkgname}/dump-gc) = %{version}

%description -n %{name}+dump-gc
This metapackage enables feature "dump-gc" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-gc-free
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-gc-free"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-gc-free) >= 0.8.1
Provides:       crate(%{pkgname}/dump-gc-free) = %{version}

%description -n %{name}+dump-gc-free
This metapackage enables feature "dump-gc-free" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-leaks
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-leaks"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-leaks) >= 0.8.1
Provides:       crate(%{pkgname}/dump-leaks) = %{version}

%description -n %{name}+dump-leaks
This metapackage enables feature "dump-leaks" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-mem
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-mem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-mem) >= 0.8.1
Provides:       crate(%{pkgname}/dump-mem) = %{version}

%description -n %{name}+dump-mem
This metapackage enables feature "dump-mem" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-module-resolve
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-module-resolve"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-module-resolve) >= 0.8.1
Provides:       crate(%{pkgname}/dump-module-resolve) = %{version}

%description -n %{name}+dump-module-resolve
This metapackage enables feature "dump-module-resolve" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-objects
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-objects"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-objects) >= 0.8.1
Provides:       crate(%{pkgname}/dump-objects) = %{version}

%description -n %{name}+dump-objects
This metapackage enables feature "dump-objects" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-promise
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-promise"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-promise) >= 0.8.1
Provides:       crate(%{pkgname}/dump-promise) = %{version}

%description -n %{name}+dump-promise
This metapackage enables feature "dump-promise" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-read-object
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-read-object"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-read-object) >= 0.8.1
Provides:       crate(%{pkgname}/dump-read-object) = %{version}

%description -n %{name}+dump-read-object
This metapackage enables feature "dump-read-object" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-shapes
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-shapes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dump-shapes) >= 0.8.1
Provides:       crate(%{pkgname}/dump-shapes) = %{version}

%description -n %{name}+dump-shapes
This metapackage enables feature "dump-shapes" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dyn-load
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dyn-load"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/dyn-load) >= 0.8.1
Provides:       crate(%{pkgname}/dyn-load) = %{version}

%description -n %{name}+dyn-load
This metapackage enables feature "dyn-load" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either
Summary:        High level bindings to the QuickJS JavaScript engine - feature "either"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/either-rs) = %{version}
Requires:       crate(rquickjs-core-0.8/either) >= 0.8.1
Provides:       crate(%{pkgname}/either) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either-rs
Summary:        High level bindings to the QuickJS JavaScript engine - feature "either-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/either-rs) = %{version}

%description -n %{name}+either-rs
This metapackage enables feature "either-rs" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        High level bindings to the QuickJS JavaScript engine - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/allocator) = %{version}
Requires:       crate(%{pkgname}/array-buffer) = %{version}
Requires:       crate(%{pkgname}/chrono) = %{version}
Requires:       crate(%{pkgname}/classes) = %{version}
Requires:       crate(%{pkgname}/dyn-load) = %{version}
Requires:       crate(%{pkgname}/either) = %{version}
Requires:       crate(%{pkgname}/indexmap) = %{version}
Requires:       crate(%{pkgname}/loader) = %{version}
Requires:       crate(%{pkgname}/macro) = %{version}
Requires:       crate(%{pkgname}/phf) = %{version}
Requires:       crate(%{pkgname}/properties) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full-async
Summary:        High level bindings to the QuickJS JavaScript engine - feature "full-async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/full) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Provides:       crate(%{pkgname}/full-async) = %{version}

%description -n %{name}+full-async
This metapackage enables feature "full-async" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        High level bindings to the QuickJS JavaScript engine - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/futures) >= 0.8.1
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        High level bindings to the QuickJS JavaScript engine - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/indexmap-rs) = %{version}
Requires:       crate(rquickjs-core-0.8/indexmap) >= 0.8.1
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap-rs
Summary:        High level bindings to the QuickJS JavaScript engine - feature "indexmap-rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap-rs) = %{version}

%description -n %{name}+indexmap-rs
This metapackage enables feature "indexmap-rs" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loader
Summary:        High level bindings to the QuickJS JavaScript engine - feature "loader"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/loader) >= 0.8.1
Provides:       crate(%{pkgname}/loader) = %{version}

%description -n %{name}+loader
This metapackage enables feature "loader" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        High level bindings to the QuickJS JavaScript engine - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/parallel) >= 0.8.1
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf
Summary:        High level bindings to the QuickJS JavaScript engine - feature "phf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/phf) >= 0.8.1
Requires:       crate(rquickjs-macro-0.8/phf) >= 0.8.1
Provides:       crate(%{pkgname}/phf) = %{version}

%description -n %{name}+phf
This metapackage enables feature "phf" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+properties
Summary:        High level bindings to the QuickJS JavaScript engine - feature "properties"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/properties) >= 0.8.1
Provides:       crate(%{pkgname}/properties) = %{version}

%description -n %{name}+properties
This metapackage enables feature "properties" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rquickjs-macro
Summary:        High level bindings to the QuickJS JavaScript engine - feature "rquickjs-macro" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-macro-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/macro) = %{version}
Provides:       crate(%{pkgname}/rquickjs-macro) = %{version}

%description -n %{name}+rquickjs-macro
This metapackage enables feature "rquickjs-macro" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "macro" feature.

%package     -n %{name}+rust-alloc
Summary:        High level bindings to the QuickJS JavaScript engine - feature "rust-alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-core-0.8/rust-alloc) >= 0.8.1
Provides:       crate(%{pkgname}/rust-alloc) = %{version}

%description -n %{name}+rust-alloc
This metapackage enables feature "rust-alloc" for the Rust rquickjs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
