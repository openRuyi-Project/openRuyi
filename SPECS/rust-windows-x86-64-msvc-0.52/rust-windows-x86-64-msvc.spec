# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}
%global __debug_install_post %{nil}

%global crate_name windows_x86_64_msvc
%global full_version 0.52.6
%global pkgname windows-x86-64-msvc-0.52

Name:           rust-windows-x86-64-msvc-0.52
Version:        0.52.6
Release:        %autorelease
Summary:        Rust crate "windows_x86_64_msvc"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:589f6da84c646204747d1270a2a5661ea66ed1cced2631d546fdfb155959f9ec
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "windows_x86_64_msvc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
