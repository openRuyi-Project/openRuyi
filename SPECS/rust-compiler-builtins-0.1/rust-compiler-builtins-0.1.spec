# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name compiler_builtins
%global full_version 0.1.160
%global pkgname compiler-builtins-0.1

Name:           rust-compiler-builtins-0.1
Version:        0.1.160
Release:        %autorelease
Summary:        Rust crate "compiler_builtins"
License:        MIT AND Apache-2.0 WITH LLVM-exception AND (MIT OR Apache-2.0)
URL:            https://github.com/rust-lang/compiler-builtins
#!RemoteAsset:  sha256:6376049cfa92c0aa8b9ac95fae22184b981c658208d4ed8a1dc553cd83612895
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/mangled-names) = %{version}
Provides:       crate(%{pkgname}/mem) = %{version}
Provides:       crate(%{pkgname}/no-asm) = %{version}
Provides:       crate(%{pkgname}/no-f16-f128) = %{version}
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}
Provides:       crate(%{pkgname}/unstable-public-internals) = %{version}

%description
Source code for takopackized Rust crate "compiler_builtins"

%package     -n %{name}+c
Summary:        Compiler intrinsics used by the Rust compiler - feature "c"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/c) = %{version}

%description -n %{name}+c
This metapackage enables feature "c" for the Rust compiler_builtins crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
