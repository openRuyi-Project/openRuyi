# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic-prost
%global full_version 0.14.2
%global pkgname tonic-prost-0.14

Name:           rust-tonic-prost-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "tonic-prost"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:66bd50ad6ce1252d87ef024b3d64fe4c3cf54a86fb9ef4c631fdd0ded7aeaa67
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(prost-0.14/default) >= 0.14.0
Requires:       crate(tonic-0.14) >= 0.14.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tonic-prost"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
