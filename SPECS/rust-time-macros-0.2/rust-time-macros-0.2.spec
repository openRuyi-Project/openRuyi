# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name time-macros
%global full_version 0.2.32
%global pkgname time-macros-0.2

Name:           rust-time-macros-0.2
Version:        0.2.32
Release:        %autorelease
Summary:        Rust crate "time-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/time-rs/time
#!RemoteAsset:  sha256:7e689342a48d2ea927c87ea50cabf8594854bf940e9310208848d680d668ed85
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-conv-0.2/default) >= 0.2.2
Requires:       crate(time-core-0.1/default) >= 0.1.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/formatting) = %{version}
Provides:       crate(%{pkgname}/large-dates) = %{version}
Provides:       crate(%{pkgname}/parsing) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description
This crate is an implementation detail and should not be relied upon directly.
Source code for takopackized Rust crate "time-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
