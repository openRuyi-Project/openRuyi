# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-bidi-mirroring
%global full_version 0.4.0
%global pkgname unicode-bidi-mirroring-0.4

Name:           rust-unicode-bidi-mirroring-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "unicode-bidi-mirroring"
License:        MIT OR Apache-2.0
URL:            https://github.com/RazrFalcon/unicode-bidi-mirroring
#!RemoteAsset:  sha256:5dfa6e8c60bb66d49db113e0125ee8711b7647b5579dc7f5f19c42357ed039fe
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "unicode-bidi-mirroring"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
