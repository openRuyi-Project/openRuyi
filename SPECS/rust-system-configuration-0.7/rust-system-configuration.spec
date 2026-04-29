# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name system-configuration
%global full_version 0.7.0
%global pkgname system-configuration-0.7

Name:           rust-system-configuration-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "system-configuration"
License:        MIT OR Apache-2.0
URL:            https://github.com/mullvad/system-configuration-rs
#!RemoteAsset:  sha256:a13f3d0daba03132c0aa9767f98351b3488edc2c100cda2d2ec2b04f3d8d3c8b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.0
Requires:       crate(core-foundation-0.9/default) >= 0.9.4
Requires:       crate(system-configuration-sys-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "system-configuration"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
