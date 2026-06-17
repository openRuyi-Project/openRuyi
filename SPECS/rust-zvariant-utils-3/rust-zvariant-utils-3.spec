# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zvariant_utils
%global full_version 3.3.1
%global pkgname zvariant-utils-3

Name:           rust-zvariant-utils-3
Version:        3.3.1
Release:        %autorelease
Summary:        Rust crate "zvariant_utils"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:6d464f5733ffa07a3164d656f18533caace9d0638596721355d73256a410d691
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.81
Requires:       crate(quote-1/default) >= 1.0.36
Requires:       crate(serde-1/default) >= 1.0.200
Requires:       crate(serde-1/derive) >= 1.0.200
Requires:       crate(syn-2/default) >= 2.0.64
Requires:       crate(syn-2/extra-traits) >= 2.0.64
Requires:       crate(syn-2/full) >= 2.0.64
Requires:       crate(winnow-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gvariant) = %{version}

%description
Source code for takopackized Rust crate "zvariant_utils"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
