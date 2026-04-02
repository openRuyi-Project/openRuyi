# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name android_system_properties
%global full_version 0.1.5
%global pkgname android-system-properties-0.1

Name:           rust-android-system-properties-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "android_system_properties"
License:        MIT/Apache-2.0
URL:            https://github.com/nical/android_system_properties
#!RemoteAsset:  sha256:819e7219dbd41043ac279b19830f2efc897156490d7fd6ea916720117ee66311
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "android_system_properties"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
