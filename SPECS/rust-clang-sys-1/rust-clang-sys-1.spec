# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clang-sys
%global full_version 1.8.1
%global pkgname clang-sys-1

Name:           rust-clang-sys-1
Version:        1.8.1
Release:        %autorelease
Summary:        Rust crate "clang-sys"
License:        Apache-2.0
URL:            https://github.com/KyleMayes/clang-sys
#!RemoteAsset:  sha256:0b023947811758c97c59bf9d1c188fd619ad4718dcaa767947df1cadb14f39f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glob-0.3) >= 0.3.0
Requires:       crate(glob-0.3/default) >= 0.3.0
Requires:       crate(libc-0.2) >= 0.2.39
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clang-10-0) = %{version}
Provides:       crate(%{pkgname}/clang-11-0) = %{version}
Provides:       crate(%{pkgname}/clang-12-0) = %{version}
Provides:       crate(%{pkgname}/clang-13-0) = %{version}
Provides:       crate(%{pkgname}/clang-14-0) = %{version}
Provides:       crate(%{pkgname}/clang-15-0) = %{version}
Provides:       crate(%{pkgname}/clang-16-0) = %{version}
Provides:       crate(%{pkgname}/clang-17-0) = %{version}
Provides:       crate(%{pkgname}/clang-18-0) = %{version}
Provides:       crate(%{pkgname}/clang-3-5) = %{version}
Provides:       crate(%{pkgname}/clang-3-6) = %{version}
Provides:       crate(%{pkgname}/clang-3-7) = %{version}
Provides:       crate(%{pkgname}/clang-3-8) = %{version}
Provides:       crate(%{pkgname}/clang-3-9) = %{version}
Provides:       crate(%{pkgname}/clang-4-0) = %{version}
Provides:       crate(%{pkgname}/clang-5-0) = %{version}
Provides:       crate(%{pkgname}/clang-6-0) = %{version}
Provides:       crate(%{pkgname}/clang-7-0) = %{version}
Provides:       crate(%{pkgname}/clang-8-0) = %{version}
Provides:       crate(%{pkgname}/clang-9-0) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/libcpp) = %{version}
Provides:       crate(%{pkgname}/static) = %{version}

%description
Source code for takopackized Rust crate "clang-sys"

%package     -n %{name}+libloading
Summary:        Rust bindings for libclang - feature "libloading" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libloading-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/libloading) = %{version}
Provides:       crate(%{pkgname}/runtime) = %{version}

%description -n %{name}+libloading
This metapackage enables feature "libloading" for the Rust clang-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "runtime" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
