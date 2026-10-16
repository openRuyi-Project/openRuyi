# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name doctest-file
%global full_version 1.1.1
%global pkgname doctest-file-1

Name:           rust-doctest-file-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "doctest-file"
License:        0BSD
URL:            https://codeberg.org/Goat7658/doctest-file
#!RemoteAsset:  sha256:c2db04e74f0a9a93103b50e90b96024c9b2bdca8bce6a632ec71b88736d3d359
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "doctest-file"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
