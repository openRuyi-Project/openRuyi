# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name endian-type
%global full_version 0.2.0
%global pkgname endian-type-0.2

Name:           rust-endian-type-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "endian-type"
License:        MIT
URL:            https://github.com/Lolirofle/endian-type.git
#!RemoteAsset:  sha256:869b0adbda23651a9c5c0c3d270aac9fcb52e8622a8f2b17e57802d7791962f2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "endian-type"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
