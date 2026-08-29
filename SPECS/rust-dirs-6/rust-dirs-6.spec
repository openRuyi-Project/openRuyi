# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs
%global full_version 6.0.0
%global pkgname dirs-6

Name:           rust-dirs-6
Version:        6.0.0
Release:        %autorelease
Summary:        Rust crate "dirs"
License:        MIT OR Apache-2.0
URL:            https://github.com/soc/dirs-rs
#!RemoteAsset:  sha256:c3e8aa94d75141228480295a7d0e7feb620b1a5ad9f12bc40be62411e38cce4e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-sys-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dirs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
