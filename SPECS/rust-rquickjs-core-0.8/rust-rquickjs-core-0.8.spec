# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rquickjs-core
%global full_version 0.8.1
%global pkgname rquickjs-core-0.8

Name:           rust-rquickjs-core-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "rquickjs-core"
License:        MIT
URL:            https://github.com/DelSkayn/rquickjs.git
#!RemoteAsset:  sha256:6c8db6379e204ef84c0811e90e7cc3e3e4d7688701db68a00d14a6db6849087b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rquickjs-sys-0.8/default) >= 0.8.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/allocator) = %{version}
Provides:       crate(%{pkgname}/array-buffer) = %{version}
Provides:       crate(%{pkgname}/classes) = %{version}
Provides:       crate(%{pkgname}/compile-tests) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/doc-cfg) = %{version}
Provides:       crate(%{pkgname}/multi-ctx) = %{version}
Provides:       crate(%{pkgname}/parallel) = %{version}
Provides:       crate(%{pkgname}/properties) = %{version}
Provides:       crate(%{pkgname}/rust-alloc) = %{version}

%description
Source code for takopackized Rust crate "rquickjs-core"

%package     -n %{name}+bindgen
Summary:        High level bindings to the QuickJS JavaScript engine - feature "bindgen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/bindgen) >= 0.8.1
Provides:       crate(%{pkgname}/bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        High level bindings to the QuickJS JavaScript engine - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dlopen
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dlopen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dlopen-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/dlopen) = %{version}

%description -n %{name}+dlopen
This metapackage enables feature "dlopen" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-atoms
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-atoms"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-atoms) >= 0.8.1
Provides:       crate(%{pkgname}/dump-atoms) = %{version}

%description -n %{name}+dump-atoms
This metapackage enables feature "dump-atoms" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-bytecode
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-bytecode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-bytecode) >= 0.8.1
Provides:       crate(%{pkgname}/dump-bytecode) = %{version}

%description -n %{name}+dump-bytecode
This metapackage enables feature "dump-bytecode" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-free
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-free"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-free) >= 0.8.1
Provides:       crate(%{pkgname}/dump-free) = %{version}

%description -n %{name}+dump-free
This metapackage enables feature "dump-free" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-gc
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-gc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-gc) >= 0.8.1
Provides:       crate(%{pkgname}/dump-gc) = %{version}

%description -n %{name}+dump-gc
This metapackage enables feature "dump-gc" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-gc-free
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-gc-free"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-gc-free) >= 0.8.1
Provides:       crate(%{pkgname}/dump-gc-free) = %{version}

%description -n %{name}+dump-gc-free
This metapackage enables feature "dump-gc-free" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-leaks
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-leaks"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-leaks) >= 0.8.1
Provides:       crate(%{pkgname}/dump-leaks) = %{version}

%description -n %{name}+dump-leaks
This metapackage enables feature "dump-leaks" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-mem
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-mem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-mem) >= 0.8.1
Provides:       crate(%{pkgname}/dump-mem) = %{version}

%description -n %{name}+dump-mem
This metapackage enables feature "dump-mem" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-module-resolve
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-module-resolve"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-module-resolve) >= 0.8.1
Provides:       crate(%{pkgname}/dump-module-resolve) = %{version}

%description -n %{name}+dump-module-resolve
This metapackage enables feature "dump-module-resolve" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-objects
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-objects"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-objects) >= 0.8.1
Provides:       crate(%{pkgname}/dump-objects) = %{version}

%description -n %{name}+dump-objects
This metapackage enables feature "dump-objects" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-promise
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-promise"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-promise) >= 0.8.1
Provides:       crate(%{pkgname}/dump-promise) = %{version}

%description -n %{name}+dump-promise
This metapackage enables feature "dump-promise" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-read-object
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-read-object"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-read-object) >= 0.8.1
Provides:       crate(%{pkgname}/dump-read-object) = %{version}

%description -n %{name}+dump-read-object
This metapackage enables feature "dump-read-object" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dump-shapes
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dump-shapes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rquickjs-sys-0.8/dump-shapes) >= 0.8.1
Provides:       crate(%{pkgname}/dump-shapes) = %{version}

%description -n %{name}+dump-shapes
This metapackage enables feature "dump-shapes" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dyn-load
Summary:        High level bindings to the QuickJS JavaScript engine - feature "dyn-load"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/dlopen) = %{version}
Requires:       crate(%{pkgname}/loader) = %{version}
Provides:       crate(%{pkgname}/dyn-load) = %{version}

%description -n %{name}+dyn-load
This metapackage enables feature "dyn-load" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either
Summary:        High level bindings to the QuickJS JavaScript engine - feature "either"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/either) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

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
Requires:       crate(%{pkgname}/properties) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full-async
Summary:        High level bindings to the QuickJS JavaScript engine - feature "full-async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/full) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Provides:       crate(%{pkgname}/full-async) = %{version}

%description -n %{name}+full-async
This metapackage enables feature "full-async" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        High level bindings to the QuickJS JavaScript engine - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-lock-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        High level bindings to the QuickJS JavaScript engine - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf
Summary:        High level bindings to the QuickJS JavaScript engine - feature "phf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/phf) = %{version}

%description -n %{name}+phf
This metapackage enables feature "phf" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+relative-path
Summary:        High level bindings to the QuickJS JavaScript engine - feature "relative-path" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(relative-path-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/loader) = %{version}
Provides:       crate(%{pkgname}/relative-path) = %{version}

%description -n %{name}+relative-path
This metapackage enables feature "relative-path" for the Rust rquickjs-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "loader" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
