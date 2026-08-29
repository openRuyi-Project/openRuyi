# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bindgen
%global full_version 0.69.5
%global pkgname bindgen-0.69

Name:           rust-bindgen-0.69
Version:        0.69.5
Release:        %autorelease
Summary:        Rust crate "bindgen"
License:        BSD-3-Clause
URL:            https://rust-lang.github.io/rust-bindgen/
#!RemoteAsset:  sha256:271383c67ccabffb7381723dea0672a673f292304fcb45c01cc648c7a8d58088
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.2.1
Requires:       crate(cexpr-0.6/default) >= 0.6.0
Requires:       crate(clang-sys-1/clang-6-0) >= 1.0.0
Requires:       crate(clang-sys-1/default) >= 1.0.0
Requires:       crate(itertools-0.10) >= 0.10.0
Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(lazycell-1/default) >= 1.0.0
Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(regex-1/std) >= 1.5.1
Requires:       crate(regex-1/unicode-perl) >= 1.5.1
Requires:       crate(rustc-hash-1/default) >= 1.0.1
Requires:       crate(shlex-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/visit-mut) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}
Provides:       crate(%{pkgname}/testing-only-extra-assertions) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-16) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-9) = %{version}

%description
Source code for takopackized Rust crate "bindgen"

%package     -n %{name}+default
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/prettyplease) = %{version}
Requires:       crate(%{pkgname}/runtime) = %{version}
Requires:       crate(%{pkgname}/which-rustfmt) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+experimental
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "experimental"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(annotate-snippets-0.9/color) >= 0.9.1
Requires:       crate(annotate-snippets-0.9/default) >= 0.9.1
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
Requires:       crate(clang-sys-1/clang-6-0) >= 1.0.0
Requires:       crate(clang-sys-1/runtime) >= 1.0.0
Provides:       crate(%{pkgname}/runtime) = %{version}

%description -n %{name}+runtime
This metapackage enables feature "runtime" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clang-sys-1/clang-6-0) >= 1.0.0
Requires:       crate(clang-sys-1/static) >= 1.0.0
Provides:       crate(%{pkgname}/static) = %{version}

%description -n %{name}+static
This metapackage enables feature "static" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+which-rustfmt
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "which-rustfmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(which-4) >= 4.2.1
Provides:       crate(%{pkgname}/which-rustfmt) = %{version}

%description -n %{name}+which-rustfmt
This metapackage enables feature "which-rustfmt" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
