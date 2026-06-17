# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libbz2-rs-sys
%global full_version 0.2.5
%global pkgname libbz2-rs-sys-0.2

Name:           rust-libbz2-rs-sys-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "libbz2-rs-sys"
License:        bzip2-1.0.6
URL:            https://github.com/trifectatechfoundation/libbzip2-rs
#!RemoteAsset:  sha256:34b357333733e8260735ba5894eb928c02ecc69c78715f01a8019e7fa7f2db4c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/custom-prefix) = %{version}
Provides:       crate(%{pkgname}/export-symbols) = %{version}
Provides:       crate(%{pkgname}/internal-fuzz-disable-checksum) = %{version}
Provides:       crate(%{pkgname}/rust-allocator) = %{version}
Provides:       crate(%{pkgname}/semver-prefix) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/testing-prefix) = %{version}

%description
Source code for takopackized Rust crate "libbz2-rs-sys"

%package     -n %{name}+c-allocator
Summary:        Drop-in compatible rust bzip2 implementation - feature "c-allocator" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/c-allocator) = %{version}
Provides:       crate(%{pkgname}/stdio) = %{version}

%description -n %{name}+c-allocator
This metapackage enables feature "c-allocator" for the Rust libbz2-rs-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "stdio" feature.

%package     -n %{name}+default
Summary:        Drop-in compatible rust bzip2 implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/stdio) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust libbz2-rs-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
