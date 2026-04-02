# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows_aarch64_msvc
%global full_version 0.53.1
%global pkgname windows-aarch64-msvc-0.53

Name:           rust-windows-aarch64-msvc-0.53
Version:        0.53.1
Release:        %autorelease
Summary:        Rust crate "windows_aarch64_msvc"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:b9d782e804c2f632e395708e99a94275910eb9100b2114651e04744e9b125006
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "windows_aarch64_msvc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
