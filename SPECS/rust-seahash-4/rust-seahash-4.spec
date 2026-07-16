# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name seahash
%global full_version 4.1.0
%global pkgname seahash-4

Name:           rust-seahash-4
Version:        4.1.0
Release:        %autorelease
Summary:        Rust crate "seahash"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/seahash
#!RemoteAsset:  sha256:1c107b6f4780854c8b126e228ea8869f4d7b71260f962fefb57b996b8959ba6b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description
Source code for takopackized Rust crate "seahash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
