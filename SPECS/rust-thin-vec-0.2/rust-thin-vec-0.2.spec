# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thin-vec
%global full_version 0.2.21
%global pkgname thin-vec-0.2

Name:           rust-thin-vec-0.2
Version:        0.2.21
Release:        %autorelease
Summary:        Rust crate "thin-vec"
License:        MIT OR Apache-2.0
URL:            https://github.com/mozilla/thin-vec
#!RemoteAsset:  sha256:d6a4b9ba8738cb4a4f399d37e266becfd475e75eb73425b87a05a2f2039ba63e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-new) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gecko-ffi) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "thin-vec"

%package     -n %{name}+malloc-size-of
Summary:        Vec that takes up less space on the stack - feature "malloc_size_of"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malloc-size-of-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/malloc-size-of) = %{version}

%description -n %{name}+malloc-size-of
This metapackage enables feature "malloc_size_of" for the Rust thin-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Vec that takes up less space on the stack - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust thin-vec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
