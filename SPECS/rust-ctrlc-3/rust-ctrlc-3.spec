# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctrlc
%global full_version 3.5.2
%global pkgname ctrlc-3

Name:           rust-ctrlc-3
Version:        3.5.2
Release:        %autorelease
Summary:        Rust crate "ctrlc"
License:        MIT OR Apache-2.0
URL:            https://github.com/Detegr/rust-ctrlc
#!RemoteAsset:  sha256:e0b1fab2ae45819af2d0731d60f2afe17227ebb1a1538a236da84c93e9a60162
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dispatch2-0.3/default) >= 0.3.0
Requires:       crate(nix-0.31/signal) >= 0.31.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-security) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/termination) = %{version}

%description
Source code for takopackized Rust crate "ctrlc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
