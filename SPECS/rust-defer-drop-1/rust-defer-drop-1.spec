# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name defer-drop
%global full_version 1.3.0
%global pkgname defer-drop-1

Name:           rust-defer-drop-1
Version:        1.3.0
Release:        %autorelease
Summary:        Rust crate "defer-drop"
License:        MPL-2.0
URL:            https://github.com/Lucretiel/defer-drop
#!RemoteAsset:  sha256:f613ec9fa66a6b28cdb1842b27f9adf24f39f9afc4dcdd9fdecee4aca7945c57
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.6
Requires:       crate(once-cell-1/default) >= 1.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "defer-drop"

%package     -n %{name}+serde
Summary:        Defer dropping large types to a background thread - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust defer-drop crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
