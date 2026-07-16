# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-conv
%global full_version 0.1.0
%global pkgname num-conv-0.1

Name:           rust-num-conv-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "num-conv"
License:        MIT OR Apache-2.0
URL:            https://github.com/jhpratt/num-conv
#!RemoteAsset:  sha256:51d515d32fb182ee37cda2ccdcb92950d6a3c2893aa280e540671c2cd0f3b1d9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
This provides better certainty when refactoring, makes the exact behavior of code more explicit, and allows using turbofish syntax.
Source code for takopackized Rust crate "num-conv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
