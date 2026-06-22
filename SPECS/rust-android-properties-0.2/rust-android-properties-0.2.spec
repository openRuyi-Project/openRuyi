# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name android-properties
%global full_version 0.2.2
%global pkgname android-properties-0.2

Name:           rust-android-properties-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "android-properties"
License:        MIT
URL:            https://github.com/miklelappo/android-properties
#!RemoteAsset:  sha256:fc7eb209b1518d6bb87b283c20095f5228ecda460da70b44f0802523dea6da04
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bionic-deprecated) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "android-properties"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
