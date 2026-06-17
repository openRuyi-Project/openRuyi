# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imara-diff
%global full_version 0.1.8
%global pkgname imara-diff-0.1

Name:           rust-imara-diff-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "imara-diff"
License:        Apache-2.0
URL:            https://github.com/pascalkuthe/imara-diff
#!RemoteAsset:  sha256:17d34b7d42178945f775e84bc4c36dde7c1c6cdfea656d3354d009056f2bb3d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.0
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unified-diff) = %{version}

%description
Source code for takopackized Rust crate "imara-diff"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
