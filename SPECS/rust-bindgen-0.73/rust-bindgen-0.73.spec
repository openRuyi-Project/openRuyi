# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bindgen
%global full_version 0.73.0
%global pkgname bindgen-0.73

Name:           rust-bindgen-0.73
Version:        0.73.0
Release:        %autorelease
Summary:        Rust crate "bindgen"
License:        BSD-3-Clause
URL:            https://rust-lang.github.io/rust-bindgen/
#!RemoteAsset:  sha256:bc28bda9791f9d907d05b23533298ba26af0e9e75c3f32044569707afbca17e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.2.1
Requires:       crate(cexpr-0.6/default) >= 0.6.0
Requires:       crate(clang-sys-1/clang-11-0) >= 1.0.0
Requires:       crate(clang-sys-1/runtime) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(prettyplease-0.3/default) >= 0.3.0
Requires:       crate(proc-macro2-1/default) >= 1.0.80
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(regex-1/std) >= 1.5.3
Requires:       crate(regex-1/unicode-perl) >= 1.5.3
Requires:       crate(rustc-hash-2/default) >= 2.1.0
Requires:       crate(shlex-2/default) >= 2.0.0
Requires:       crate(syn-3/default) >= 3.0.0
Requires:       crate(syn-3/extra-traits) >= 3.0.0
Requires:       crate(syn-3/full) >= 3.0.0
Requires:       crate(syn-3/visit-mut) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}
Provides:       crate(%{pkgname}/prettyplease) = %{version}
Provides:       crate(%{pkgname}/runtime) = %{version}

%description
Automatically generates Rust FFI bindings to C and C++ libraries.
Source code for takopackized Rust crate "bindgen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
