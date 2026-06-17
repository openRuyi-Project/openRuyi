# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bzip2
%global full_version 0.6.1
%global pkgname bzip2-0.6

Name:           rust-bzip2-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "bzip2"
License:        MIT OR Apache-2.0
URL:            https://github.com/trifectatechfoundation/bzip2-rs
#!RemoteAsset:  sha256:f3a53fac24f34a81bc9954b5d6cfce0c21e18ec6959f44f56e8e90e4bb7c346c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bzip2"

%package     -n %{name}+bzip2-sys
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "bzip2-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-sys-0.1/default) >= 0.1.13
Provides:       crate(%{pkgname}/bzip2-sys) = %{version}

%description -n %{name}+bzip2-sys
This metapackage enables feature "bzip2-sys" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libbz2-rs-sys-0.2/rust-allocator) >= 0.2.1
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

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
