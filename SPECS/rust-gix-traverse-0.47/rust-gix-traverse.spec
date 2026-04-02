# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-traverse
%global full_version 0.47.0
%global pkgname gix-traverse-0.47

Name:           rust-gix-traverse-0.47
Version:        0.47.0
Release:        %autorelease
Summary:        Rust crate "gix-traverse"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:c7cdc82509d792ba0ad815f86f6b469c7afe10f94362e96c4494525a6601bdd5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(gix-commitgraph-0.29/default) >= 0.29.0
Requires:       crate(gix-date-0.10/default) >= 0.10.7
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-revwalk-0.21/default) >= 0.21.0
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-traverse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
