# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-targets
%global full_version 0.42.2
%global pkgname windows-targets-0.42

Name:           rust-windows-targets-0.42
Version:        0.42.2
Release:        %autorelease
Summary:        Rust crate "windows-targets"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:8e5180c00cd44c9b1c88adb3693291f1cd93605ded80c250a75d472756b4d071
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-aarch64-gnullvm-0.42/default) >= 0.42.2
Requires:       crate(windows-aarch64-msvc-0.42/default) >= 0.42.2
Requires:       crate(windows-i686-gnu-0.42/default) >= 0.42.2
Requires:       crate(windows-i686-msvc-0.42/default) >= 0.42.2
Requires:       crate(windows-x86-64-gnu-0.42/default) >= 0.42.2
Requires:       crate(windows-x86-64-gnullvm-0.42/default) >= 0.42.2
Requires:       crate(windows-x86-64-msvc-0.42/default) >= 0.42.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows-targets"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
