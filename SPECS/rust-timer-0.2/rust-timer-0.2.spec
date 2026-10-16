# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name timer
%global full_version 0.2.0
%global pkgname timer-0.2

Name:           rust-timer-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "timer"
License:        MPL-2.0
URL:            https://github.com/Yoric/timer.rs
#!RemoteAsset:  sha256:31d42176308937165701f50638db1c31586f183f1aab416268216577aec7306b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(chrono-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Use it to schedule execution of closures after a delay or at a given timestamp.
Source code for takopackized Rust crate "timer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
