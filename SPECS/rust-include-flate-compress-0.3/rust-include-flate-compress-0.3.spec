# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name include-flate-compress
%global full_version 0.3.4
%global pkgname include-flate-compress-0.3

Name:           rust-include-flate-compress-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "include-flate-compress"
License:        Apache-2.0
URL:            https://github.com/SOF3/include-flate
#!RemoteAsset:  sha256:44fbb9c5ccb9a5b67b4afa2974c27e5507ea1bf6d22828cef418e4dfaeca51dd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "include-flate-compress"

%package     -n %{name}+default
Summary:        Compression algorithm provider - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust include-flate-compress crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Compression algorithm provider - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libflate-2/default) >= 2.3.0
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust include-flate-compress crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Compression algorithm provider - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13/default) >= 0.13.3
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust include-flate-compress crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
