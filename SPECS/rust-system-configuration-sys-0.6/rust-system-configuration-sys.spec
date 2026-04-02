# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name system-configuration-sys
%global full_version 0.6.0
%global pkgname system-configuration-sys-0.6

Name:           rust-system-configuration-sys-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "system-configuration-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/mullvad/system-configuration-rs
#!RemoteAsset:  sha256:8e1d1b10ced5ca923a1fcb8d03e96b8d3268065d724548c0211415ff6ac6bac4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.7
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "system-configuration-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
