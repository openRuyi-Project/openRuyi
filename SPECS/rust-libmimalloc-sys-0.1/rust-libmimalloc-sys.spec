# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libmimalloc-sys
%global full_version 0.1.47
%global pkgname libmimalloc-sys-0.1

Name:           rust-libmimalloc-sys-0.1
Version:        0.1.47
Release:        %autorelease
Summary:        Rust crate "libmimalloc-sys"
License:        MIT
URL:            https://github.com/purpleprotocol/mimalloc_rust/tree/master/libmimalloc-sys
#!RemoteAsset:  sha256:2d1eacfa31c33ec25e873c136ba5669f00f9866d0688bea7be4d3f7e43067df6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.38
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/arena)
Provides:       crate(%{pkgname}/debug)
Provides:       crate(%{pkgname}/debug-in-debug)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/local-dynamic-tls)
Provides:       crate(%{pkgname}/no-thp)
Provides:       crate(%{pkgname}/override)
Provides:       crate(%{pkgname}/secure)
Provides:       crate(%{pkgname}/v2)

%description
Source code for takopackized Rust crate "libmimalloc-sys"

%package     -n %{name}+cty
Summary:        Sys crate wrapping the mimalloc allocator - feature "cty" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(cty-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/cty)
Provides:       crate(%{pkgname}/extended)

%description -n %{name}+cty
This metapackage enables feature "cty" for the Rust libmimalloc-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "extended" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
