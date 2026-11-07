# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core_arch
%global full_version 0.1.5
%global pkgname core-arch-0.1

Name:           rust-core-arch-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "core_arch"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/stdsimd
#!RemoteAsset:  sha256:3552dd3c0d542ada1688e40346b40c3ccd9cebd7da9272c566c101b953de6d13
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "core_arch"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
