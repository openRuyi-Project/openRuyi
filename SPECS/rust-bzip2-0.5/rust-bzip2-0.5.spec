# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bzip2
%global full_version 0.5.2
%global pkgname bzip2-0.5

Name:           rust-bzip2-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "bzip2"
License:        MIT OR Apache-2.0
URL:            https://github.com/trifectatechfoundation/bzip2-rs
#!RemoteAsset:  sha256:49ecfb22d906f800d4fe833b6282cf4dc1c298f5057ca0b5445e5c209735ca47
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bzip2"

%package     -n %{name}+default
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-sys-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libbz2-rs-sys
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "libbz2-rs-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-sys-0.1/disabled) >= 0.1.13
Requires:       crate(libbz2-rs-sys-0.1/rust-allocator) >= 0.1.3
Requires:       crate(libbz2-rs-sys-0.1/semver-prefix) >= 0.1.3
Provides:       crate(%{pkgname}/libbz2-rs-sys) = %{version}

%description -n %{name}+libbz2-rs-sys
This metapackage enables feature "libbz2-rs-sys" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-sys-0.1/static) >= 0.1.13
Provides:       crate(%{pkgname}/static) = %{version}

%description -n %{name}+static
This metapackage enables feature "static" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
