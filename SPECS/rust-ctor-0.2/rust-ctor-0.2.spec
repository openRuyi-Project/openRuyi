# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctor
%global full_version 0.2.9
%global pkgname ctor-0.2

Name:           rust-ctor-0.2
Version:        0.2.9
Release:        %autorelease
Summary:        Rust crate "ctor"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/rust-ctor
#!RemoteAsset:  sha256:32a2785755761f3ddc1492979ce1e48d2c00d09311c39e4466429188f3dd6501
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.20
Requires:       crate(syn-2/full) >= 2.0.12
Requires:       crate(syn-2/parsing) >= 2.0.12
Requires:       crate(syn-2/printing) >= 2.0.12
Requires:       crate(syn-2/proc-macro) >= 2.0.12

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/used-linker) = %{version}

%description
Source code for takopackized Rust crate "ctor"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
