# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jobserver
%global full_version 0.1.35
%global pkgname jobserver-0.1

Name:           rust-jobserver-0.1
Version:        0.1.35
Release:        %autorelease
Summary:        Rust crate "jobserver"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/jobserver-rs
#!RemoteAsset:  sha256:1c00acbd29eabad4a2392fa0e921c874934dbbf4194312ad20f04a0ed67a3cb3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(getrandom-0.4/std) >= 0.4.0
Requires:       crate(libc-0.2/default) >= 0.2.171

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "jobserver"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
