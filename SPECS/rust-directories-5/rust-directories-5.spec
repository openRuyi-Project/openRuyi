# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name directories
%global full_version 5.0.1
%global pkgname directories-5

Name:           rust-directories-5
Version:        5.0.1
Release:        %autorelease
Summary:        Rust crate "directories"
License:        MIT OR Apache-2.0
URL:            https://github.com/soc/directories-rs
#!RemoteAsset:  sha256:9a49173b84e034382284f27f1af4dcbbd231ffa358c0fe316541a7337f376a35
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-sys-0.4/default) >= 0.4.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "directories"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
