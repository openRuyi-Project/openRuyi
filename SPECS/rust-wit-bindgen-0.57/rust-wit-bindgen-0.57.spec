# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wit-bindgen
%global full_version 0.57.1
%global pkgname wit-bindgen-0.57

Name:           rust-wit-bindgen-0.57
Version:        0.57.1
Release:        %autorelease
Summary:        Rust crate "wit-bindgen"
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://github.com/bytecodealliance/wit-bindgen
#!RemoteAsset:  sha256:1ebf944e87a7c253233ad6766e082e3cd714b5d03812acc24c318f549614536e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/inter-task-wakeup) = %{version}
Provides:       crate(%{pkgname}/realloc) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Used when compiling Rust programs to the component model.
Source code for takopackized Rust crate "wit-bindgen"

%package     -n %{name}+async-spawn
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "async-spawn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.30
Provides:       crate(%{pkgname}/async-spawn) = %{version}

%description -n %{name}+async-spawn
Used when compiling Rust programs to the component model.
This metapackage enables feature "async-spawn" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/default) >= 2.11.1
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
Used when compiling Rust programs to the component model.
This metapackage enables feature "bitflags" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/macro-string) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/realloc) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Used when compiling Rust programs to the component model.
This metapackage enables feature "default" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-stream
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "futures-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.30
Provides:       crate(%{pkgname}/futures-stream) = %{version}

%description -n %{name}+futures-stream
Used when compiling Rust programs to the component model.
This metapackage enables feature "futures-stream" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macro-string
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "macro-string"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wit-bindgen-rust-macro-0.57/macro-string) >= 0.57.1
Provides:       crate(%{pkgname}/macro-string) = %{version}

%description -n %{name}+macro-string
Used when compiling Rust programs to the component model.
This metapackage enables feature "macro-string" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Rust bindings generator and runtime support for WIT and the component model - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wit-bindgen-rust-macro-0.57) >= 0.57.1
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
Used when compiling Rust programs to the component model.
This metapackage enables feature "macros" for the Rust wit-bindgen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
