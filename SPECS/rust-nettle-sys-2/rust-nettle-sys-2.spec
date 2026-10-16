# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nettle-sys
%global full_version 2.3.2
%global pkgname nettle-sys-2

Name:           rust-nettle-sys-2
Version:        2.3.2
Release:        %autorelease
Summary:        Rust crate "nettle-sys"
License:        LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://gitlab.com/sequoia-pgp/nettle-sys
#!RemoteAsset:  sha256:f35502358aa77e598570bbf9a79ad19c4985a1bcd157b5d70197688dafca9b48
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bindgen-0.72) >= 0.72.1
Requires:       crate(bindgen-0.72/runtime) >= 0.72.1
Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pkg-config-0.3) >= 0.3.0
Requires:       crate(tempfile-3) >= 3.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "nettle-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
