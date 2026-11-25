# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aligned_box
%global full_version 0.3.0
%global pkgname aligned-box-0.3

Name:           rust-aligned-box-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "aligned_box"
License:        MIT
URL:            https://github.com/michaellass/aligned_box/
#!RemoteAsset:  sha256:5ebdec4a15fc241b75eb9a55d320cef51549f95f739f8ce3dce24b19b9e5f24a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "aligned_box"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
