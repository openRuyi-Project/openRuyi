# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bitstream-io
%global full_version 4.10.0
%global pkgname bitstream-io-4

Name:           rust-bitstream-io-4
Version:        4.10.0
Release:        %autorelease
Summary:        Rust crate "bitstream-io"
License:        MIT OR Apache-2.0
URL:            https://github.com/tuffy/bitstream-io
#!RemoteAsset:  sha256:7eff00be299a18769011411c9def0d827e8f2d7bf0c3dbf53633147a8867fd1f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(no-std-io2-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bitstream-io"

%package     -n %{name}+alloc
Summary:        Reading/writing un-aligned values from/to streams in big-endian and little-endian formats - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(no-std-io2-0.9/alloc) >= 0.9.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bitstream-io crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Reading/writing un-aligned values from/to streams in big-endian and little-endian formats - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(no-std-io2-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bitstream-io crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
