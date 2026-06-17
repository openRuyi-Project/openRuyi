# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name endian-type
%global full_version 0.1.2
%global pkgname endian-type-0.1

Name:           rust-endian-type-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "endian-type"
License:        MIT
URL:            https://github.com/Lolirofle/endian-type
#!RemoteAsset:  sha256:c34f04666d835ff5d62e058c3995147c06f42fe86ff053337632bca83e42702d
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
