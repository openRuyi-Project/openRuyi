# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hermit-abi
%global full_version 0.1.19
%global pkgname hermit-abi-0.1

Name:           rust-hermit-abi-0.1
Version:        0.1.19
Release:        %autorelease
Summary:        Rust crate "hermit-abi"
License:        MIT OR Apache-2.0
URL:            https://github.com/hermitcore/libhermit-rs
#!RemoteAsset:  sha256:62b467343b94ba476dcb2500d242dadbb39557df889310ac77c5d99100aaac33
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.51
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/docs) = %{version}

%description
It is used to build the target `x86_64-unknown-hermit`.
Source code for takopackized Rust crate "hermit-abi"

%package     -n %{name}+compiler-builtins
Summary:        Small interface to call functions from the unikernel RustyHermit - feature "compiler_builtins"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(compiler-builtins-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/compiler-builtins) = %{version}

%description -n %{name}+compiler-builtins
It is used to build the target `x86_64-unknown-hermit`.
This metapackage enables feature "compiler_builtins" for the Rust hermit-abi crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-dep-of-std
Summary:        Small interface to call functions from the unikernel RustyHermit - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(compiler-builtins-0.1/rustc-dep-of-std) >= 0.1.0
Requires:       crate(libc-0.2/rustc-dep-of-std) >= 0.2.51
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
It is used to build the target `x86_64-unknown-hermit`.
This metapackage enables feature "rustc-dep-of-std" for the Rust hermit-abi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
