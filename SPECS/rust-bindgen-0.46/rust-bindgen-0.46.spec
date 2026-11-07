# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bindgen
%global full_version 0.46.0
%global pkgname bindgen-0.46

Name:           rust-bindgen-0.46
Version:        0.46.0
Release:        %autorelease
Summary:        Rust crate "bindgen"
License:        BSD-3-Clause
URL:            https://rust-lang.github.io/rust-bindgen/
#!RemoteAsset:  sha256:8f7f7f0701772b17de73e4f5cbcb1dd6926f4706cba4c1ab62c5367f8bdc94e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.3
Requires:       crate(cexpr-0.3/default) >= 0.3.3
Requires:       crate(cfg-if-0.1/default) >= 0.1.0
Requires:       crate(clang-sys-0.26/clang-6-0) >= 0.26.0
Requires:       crate(clang-sys-0.26/default) >= 0.26.0
Requires:       crate(clang-sys-0.26/runtime) >= 0.26.0
Requires:       crate(clap-2/default) >= 2.0.0
Requires:       crate(hashbrown-0.1/default) >= 0.1.0
Requires:       crate(lazy-static-1/default) >= 1.0.0
Requires:       crate(peeking-take-while-0.1/default) >= 0.1.2
Requires:       crate(proc-macro2-0.4) >= 0.4.0
Requires:       crate(quote-0.6) >= 0.6.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(which-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/static) = %{version}
Provides:       crate(%{pkgname}/testing-only-docs) = %{version}
Provides:       crate(%{pkgname}/testing-only-extra-assertions) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-3-8) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-3-9) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-4) = %{version}
Provides:       crate(%{pkgname}/testing-only-libclang-5) = %{version}

%description
Source code for takopackized Rust crate "bindgen"

%package     -n %{name}+env-logger
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "env_logger"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(env-logger-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/env-logger) = %{version}

%description -n %{name}+env-logger
This metapackage enables feature "env_logger" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries - feature "logging" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/env-logger) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust bindgen crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
