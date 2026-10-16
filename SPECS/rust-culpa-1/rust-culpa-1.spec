# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name culpa
%global full_version 1.0.2
%global pkgname culpa-1

Name:           rust-culpa-1
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "culpa"
License:        MIT OR Apache-2.0
URL:            https://github.com/Nullus157/culpa
#!RemoteAsset:  sha256:5ae0bfe9317b1cb4ff5a56d766ee4b157b3e1f47f11979253570e88d10fd1fd3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(culpa-macros-1/default) >= 1.0.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "culpa"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
