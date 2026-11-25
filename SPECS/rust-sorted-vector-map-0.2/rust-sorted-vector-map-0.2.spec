# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sorted_vector_map
%global full_version 0.2.1
%global pkgname sorted-vector-map-0.2

Name:           rust-sorted-vector-map-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "sorted_vector_map"
License:        MIT OR Apache-2.0
URL:            https://github.com/facebookexperimental/rust-shed
#!RemoteAsset:  sha256:94bf565ee1681b4473aa5a9d71d807347c28021bd1d8947cb626b02f42a0141f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(quickcheck-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sorted_vector_map"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
