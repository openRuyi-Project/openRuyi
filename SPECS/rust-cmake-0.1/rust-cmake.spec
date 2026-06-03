# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cmake
%global full_version 0.1.57
%global pkgname cmake-0.1

Name:           rust-cmake-0.1
Version:        0.1.57
Release:        %autorelease
Summary:        Rust crate "cmake"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cmake-rs
#!RemoteAsset:  sha256:75443c44cd6b379beb8c5b45d85d0773baf31cce901fe7bb252f4eff3008ef7d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.52
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cmake"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
