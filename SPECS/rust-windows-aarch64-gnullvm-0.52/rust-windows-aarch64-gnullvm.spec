# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
%global __debug_install_post %{nil}

%global crate_name windows_aarch64_gnullvm
%global full_version 0.52.6
%global pkgname windows-aarch64-gnullvm-0.52

Name:           rust-windows-aarch64-gnullvm-0.52
Version:        0.52.6
Release:        %autorelease
Summary:        Rust crate "windows_aarch64_gnullvm"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:32a4622180e7a0ec044bb555404c800bc9fd9ec262ec147edd5989ccd0c02cd3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "windows_aarch64_gnullvm"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
