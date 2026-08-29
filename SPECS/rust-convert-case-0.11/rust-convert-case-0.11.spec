# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name convert_case
%global full_version 0.11.0
%global pkgname convert-case-0.11

Name:           rust-convert-case-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "convert_case"
License:        MIT
URL:            https://github.com/rutrum/convert-case
#!RemoteAsset:  sha256:affbf0190ed2caf063e3def54ff444b449371d55c58e513a95ab98eca50adb49
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-segmentation-1/default) >= 1.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "convert_case"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
