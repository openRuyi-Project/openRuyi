# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tuikit
%global full_version 0.5.0
%global pkgname tuikit-0.5

Name:           rust-tuikit-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "tuikit"
License:        MIT
URL:            https://github.com/lotabout/tuikit
#!RemoteAsset:  sha256:5e19c6ab038babee3d50c8c12ff8b910bdb2196f62278776422f50390d8e53d8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.4
Requires:       crate(lazy-static-1/default) >= 1.2.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(nix-0.24/fs) >= 0.24.1
Requires:       crate(nix-0.24/poll) >= 0.24.1
Requires:       crate(nix-0.24/signal) >= 0.24.1
Requires:       crate(nix-0.24/term) >= 0.24.1
Requires:       crate(term-0.7/default) >= 0.7.0
Requires:       crate(unicode-width-0.1/default) >= 0.1.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tuikit"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
