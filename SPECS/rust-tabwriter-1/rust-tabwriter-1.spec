# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tabwriter
%global full_version 1.4.1
%global pkgname tabwriter-1

Name:           rust-tabwriter-1
Version:        1.4.1
Release:        %autorelease
Summary:        Rust crate "tabwriter"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/tabwriter
#!RemoteAsset:  sha256:fce91f2f0ec87dff7e6bcbbeb267439aa1188703003c6055193c821487400432
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ansi-formatting) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tabwriter"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
