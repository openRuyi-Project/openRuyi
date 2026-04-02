# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vcpkg
%global full_version 0.2.15
%global pkgname vcpkg-0.2

Name:           rust-vcpkg-0.2
Version:        0.2.15
Release:        %autorelease
Summary:        Rust crate "vcpkg"
License:        MIT/Apache-2.0
URL:            https://github.com/mcgoo/vcpkg-rs
#!RemoteAsset:  sha256:accd4ea62f7bb7a82fe23066fb0957d48ef677f6eeb8215f372f52e48bb32426
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "vcpkg"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
