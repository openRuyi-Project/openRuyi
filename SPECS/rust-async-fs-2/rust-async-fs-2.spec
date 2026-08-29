# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-fs
%global full_version 2.2.0
%global pkgname async-fs-2

Name:           rust-async-fs-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "async-fs"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/async-fs
#!RemoteAsset:  sha256:8034a681df4aed8b8edbd7fbe472401ecf009251c8b40556b304567052e294c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-lock-3/default) >= 3.0.0
Requires:       crate(blocking-1/default) >= 1.3.0
Requires:       crate(futures-lite-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-fs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
