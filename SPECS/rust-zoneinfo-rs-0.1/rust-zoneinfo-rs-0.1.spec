# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zoneinfo_rs
%global full_version 0.1.0
%global pkgname zoneinfo-rs-0.1

Name:           rust-zoneinfo-rs-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "zoneinfo_rs"
License:        MIT OR Apache-2.0
URL:            https://github.com/boa-dev/temporal
#!RemoteAsset:  sha256:721f887750c30871f9da485630d033cff04abdb7ce91c127bc015bdbabca22d8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.16/default) >= 0.16.0
Requires:       crate(indexmap-2/default) >= 2.11.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "zoneinfo_rs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
