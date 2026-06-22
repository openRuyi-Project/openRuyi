# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name directories
%global full_version 6.0.0
%global pkgname directories-6

Name:           rust-directories-6
Version:        6.0.0
Release:        %autorelease
Summary:        Rust crate "directories"
License:        MIT OR Apache-2.0
URL:            https://github.com/soc/directories-rs
#!RemoteAsset:  sha256:16f5094c54661b38d03bd7e50df373292118db60b585c08a411c6d840017fe7d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-sys-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "directories"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
