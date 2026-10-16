# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name globwalk
%global full_version 0.9.1
%global pkgname globwalk-0.9

Name:           rust-globwalk-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "globwalk"
License:        MIT
URL:            https://github.com/gilnaa/globwalk
#!RemoteAsset:  sha256:0bf760ebf69878d9fd8f110c89703d90ce35095324d1f1edcb595c63945ee757
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(ignore-0.4/default) >= 0.4.11
Requires:       crate(walkdir-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "globwalk"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
