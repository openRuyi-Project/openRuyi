# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-bae
%global full_version 0.2.2
%global pkgname sea-bae-0.2

Name:           rust-sea-bae-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "sea-bae"
License:        MIT
URL:            https://github.com/SeaQL/sea-bae
#!RemoteAsset:  sha256:260bbc7148a8d6818ac5032a1b9970da1a68bdd723d45b12d59f7c1bf3565e24
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4/default) >= 0.4.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sea-bae"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
