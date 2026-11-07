# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name term_size
%global full_version 0.3.2
%global pkgname term-size-0.3

Name:           rust-term-size-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "term_size"
License:        MIT OR Apache-2.0
URL:            https://github.com/kbknapp/term_size-rs.git
#!RemoteAsset:  sha256:1e4129646ca0ed8f45d09b929036bafad5377103edd06e50bf574b353d2b08d9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.20
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/processenv) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/wincon) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/travis) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "term_size"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
