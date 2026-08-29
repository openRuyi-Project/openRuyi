# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bindgen
%global full_version 0.72.1
%global pkgname bindgen-0.72

Name:           rust-bindgen-0.72
Version:        0.72.1
Release:        %autorelease
Summary:        Rust crate "bindgen"
License:        BSD-3-Clause
URL:            https://rust-lang.github.io/rust-bindgen/
#!RemoteAsset:  sha256:993776b509cfb49c750f11b8f07a46fa23e0a1386ffc01fb1e7d343efc387895
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.2.1
Requires:       crate(cexpr-0.6/default) >= 0.6.0
Requires:       crate(clang-sys-1/clang-11-0) >= 1.0.0
Requires:       crate(clang-sys-1/default) >= 1.0.0
Requires:       crate(itertools-0.10) >= 0.10.0
Requires:       crate(proc-macro2-1/default) >= 1.0.80
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(regex-1/std) >= 1.5.3
Requires:       crate(regex-1/unicode-perl) >= 1.5.3
Requires:       crate(rustc-hash-2/default) >= 2.1.0
Requires:       crate(shlex-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/visit-mut) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/testing-only-extra-assertions) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-16) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-9) = %{version}

%description
Source code for takopackized Rust crate "bindgen"

%package     -n %{name}+cli
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "__cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(clap-complete-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
This metapackage enables feature "__cli" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/prettyplease) = %{version}
Requires:       crate(%{pkgname}/runtime) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "experimental"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(annotate-snippets-0.11/default) >= 0.11.4
Provides:       crate(%{pkgname}/experimental) = %{version}

%description -n %{name}+experimental
This metapackage enables feature "experimental" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prettyplease
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "prettyplease"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prettyplease-0.2/default) >= 0.2.7
Requires:       crate(prettyplease-0.2/verbatim) >= 0.2.7
Provides:       crate(%{pkgname}/prettyplease) = %{version}

%description -n %{name}+prettyplease
This metapackage enables feature "prettyplease" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+runtime
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clang-sys-1/clang-11-0) >= 1.0.0
Requires:       crate(clang-sys-1/runtime) >= 1.0.0
Provides:       crate(%{pkgname}/runtime) = %{version}

%description -n %{name}+runtime
This metapackage enables feature "runtime" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clang-sys-1/clang-11-0) >= 1.0.0
Requires:       crate(clang-sys-1/static) >= 1.0.0
Provides:       crate(%{pkgname}/static) = %{version}

%description -n %{name}+static
This metapackage enables feature "static" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
