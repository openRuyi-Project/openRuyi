# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-targets
%global full_version 0.48.5
%global pkgname windows-targets-0.48

Name:           rust-windows-targets-0.48
Version:        0.48.5
Release:        %autorelease
Summary:        Rust crate "windows-targets"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:9a2fa6e2155d7247be68c096456083145c183cbbbc2764150dda45a87197940c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-aarch64-gnullvm-0.48/default) >= 0.48.5
Requires:       crate(windows-aarch64-msvc-0.48/default) >= 0.48.5
Requires:       crate(windows-i686-gnu-0.48/default) >= 0.48.5
Requires:       crate(windows-i686-msvc-0.48/default) >= 0.48.5
Requires:       crate(windows-x86-64-gnu-0.48/default) >= 0.48.5
Requires:       crate(windows-x86-64-gnullvm-0.48/default) >= 0.48.5
Requires:       crate(windows-x86-64-msvc-0.48/default) >= 0.48.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "windows-targets"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
