# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name discard
%global full_version 1.0.4
%global pkgname discard-1

Name:           rust-discard-1
Version:        1.0.4
Release:        %autorelease
Summary:        Rust crate "discard"
License:        MIT
URL:            https://github.com/Pauan/rust-discard
#!RemoteAsset:  sha256:212d0f5754cb6769937f4501cc0e67f4f4483c8d2c3e1e922ee9edbe4ab4c7c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "discard"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
