# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name botan-sys
%global full_version 0.10.5
%global pkgname botan-sys-0.10

Name:           rust-botan-sys-0.10
Version:        0.10.5
Release:        %autorelease
Summary:        Rust crate "botan-sys"
License:        MIT
URL:            https://botan.randombit.net/
#!RemoteAsset:  sha256:9f49dde1b8ebd2996cc41c55c39f6ef8b54e38148d8973aeba0792b87b1621ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/botan3) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description
Source code for takopackized Rust crate "botan-sys"

%package     -n %{name}+botan-src
Summary:        FFI wrapper for Botan cryptography library - feature "botan-src"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(botan-src-0.30101/default) >= 0.30101.2
Provides:       crate(%{pkgname}/botan-src) = %{version}

%description -n %{name}+botan-src
This metapackage enables feature "botan-src" for the Rust botan-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        FFI wrapper for Botan cryptography library - feature "vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/botan-src) = %{version}
Requires:       crate(%{pkgname}/botan3) = %{version}
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust botan-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
