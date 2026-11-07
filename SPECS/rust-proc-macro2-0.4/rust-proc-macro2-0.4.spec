# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro2
%global full_version 0.4.30
%global pkgname proc-macro2-0.4

Name:           rust-proc-macro2-0.4
Version:        0.4.30
Release:        %autorelease
Summary:        Rust crate "proc-macro2"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/proc-macro2
#!RemoteAsset:  sha256:cf3d2011ab5c909338f7887f4fc896d35932e29146c12c8d01da6b22a80ba759
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-xid-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/proc-macro) = %{version}
Provides:       crate(%{pkgname}/span-locations) = %{version}

%description
Comes with an option, off by default, to also reimplement itself in terms of the upstream unstable API.
Source code for takopackized Rust crate "proc-macro2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
