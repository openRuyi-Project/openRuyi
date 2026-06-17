# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-revwalk
%global full_version 0.21.0
%global pkgname gix-revwalk-0.21

Name:           rust-gix-revwalk-0.21
Version:        0.21.0
Release:        %autorelease
Summary:        Rust crate "gix-revwalk"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:06e74f91709729e099af6721bd0fa7d62f243f2005085152301ca5cdd86ec02c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-commitgraph-0.29/default) >= 0.29.0
Requires:       crate(gix-date-0.10/default) >= 0.10.3
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-object-0.50/default) >= 0.50.0
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-revwalk"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
