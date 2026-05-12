# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-bindgen
%global full_version 0.51.0
%global pkgname wit-bindgen-0.51

Name:           rust-wit-bindgen-0.51
Version:        0.51.0
Release:        %autorelease
Summary:        Rust crate "wit-bindgen"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wit-bindgen
#!RemoteAsset:  sha256:d7249219f66ced02969388cf2bb044a09756a083d0fab1e566056b04d9fbcaa5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/realloc)
Provides:       crate(%{pkgname}/std)

%description
Used when compiling Rust programs to the component model.
Source code for takopackized Rust crate "wit-bindgen"

%package     -n %{name}+async
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "async" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(wit-bindgen-rust-macro-0.51/async) >= 0.51.0
Provides:       crate(%{pkgname}/async)
Provides:       crate(%{pkgname}/inter-task-wakeup)

%description -n %{name}+async
Used when compiling Rust programs to the component model.
This metapackage enables feature "async" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "inter-task-wakeup" feature.

%package     -n %{name}+async-spawn
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "async-spawn"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(futures-0.3/default) >= 0.3.30
Provides:       crate(%{pkgname}/async-spawn)

%description -n %{name}+async-spawn
Used when compiling Rust programs to the component model.
This metapackage enables feature "async-spawn" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/default) >= 2.3.3
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
Used when compiling Rust programs to the component model.
This metapackage enables feature "bitflags" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/realloc)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
Used when compiling Rust programs to the component model.
This metapackage enables feature "default" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(wit-bindgen-rust-macro-0.51/default) >= 0.51.0
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
Used when compiling Rust programs to the component model.
This metapackage enables feature "macros" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-alloc-1.0/default) >= 1.0.0
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+rustc-dep-of-std
Used when compiling Rust programs to the component model.
This metapackage enables feature "rustc-dep-of-std" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
