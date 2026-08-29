# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cpp_demangle
%global full_version 0.4.5
%global pkgname cpp-demangle-0.4

Name:           rust-cpp-demangle-0.4
Version:        0.4.5
Release:        %autorelease
Summary:        Rust crate "cpp_demangle"
License:        MIT OR Apache-2.0
URL:            https://github.com/gimli-rs/cpp_demangle
#!RemoteAsset:  sha256:f2bb79cb74d735044c972aae58ed0aaa9a837e85b01106a54c39e42e97f62253
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}
Provides:       crate(%{pkgname}/run-libiberty-tests) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "cpp_demangle"

%package     -n %{name}+afl
Summary:        Demangling C++ symbols - feature "afl" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(afl-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/afl) = %{version}
Provides:       crate(%{pkgname}/fuzz) = %{version}

%description -n %{name}+afl
This metapackage enables feature "afl" for the Rust cpp_demangle crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fuzz" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
