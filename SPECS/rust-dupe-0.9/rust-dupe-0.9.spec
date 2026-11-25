# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dupe
%global full_version 0.9.1
%global pkgname dupe-0.9

Name:           rust-dupe-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "dupe"
License:        MIT OR Apache-2.0
URL:            https://github.com/facebookincubator/gazebo
#!RemoteAsset:  sha256:6ed2bc011db9c93fbc2b6cdb341a53737a55bafb46dbb74cf6764fc33a2fbf9c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dupe-derive-0.9/default) >= 0.9.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dupe"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
