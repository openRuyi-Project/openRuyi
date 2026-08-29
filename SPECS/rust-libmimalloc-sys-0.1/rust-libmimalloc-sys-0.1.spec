# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libmimalloc-sys
%global full_version 0.1.49
%global pkgname libmimalloc-sys-0.1

Name:           rust-libmimalloc-sys-0.1
Version:        0.1.49
Release:        %autorelease
Summary:        Rust crate "libmimalloc-sys"
License:        MIT
URL:            https://github.com/purpleprotocol/mimalloc_rust/tree/master/libmimalloc-sys
#!RemoteAsset:  sha256:6a45a52f43e1c16f667ccfe4dd8c85b7f7c204fd5e3bf46c5b0db9a5c3c0b8e9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/arena) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/debug-in-debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/local-dynamic-tls) = %{version}
Provides:       crate(%{pkgname}/no-thp) = %{version}
Provides:       crate(%{pkgname}/override) = %{version}
Provides:       crate(%{pkgname}/secure) = %{version}
Provides:       crate(%{pkgname}/v2) = %{version}
Provides:       crate(%{pkgname}/win-direct-tls) = %{version}

%description
Source code for takopackized Rust crate "libmimalloc-sys"

%package     -n %{name}+cty
Summary:        Sys crate wrapping the mimalloc allocator - feature "cty" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cty-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/cty) = %{version}
Provides:       crate(%{pkgname}/extended) = %{version}

%description -n %{name}+cty
This metapackage enables feature "cty" for the Rust libmimalloc-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "extended" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
