# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pin-project-lite
%global full_version 0.2.17
%global pkgname pin-project-lite-0.2

Name:           rust-pin-project-lite-0.2
Version:        0.2.17
Release:        %autorelease
Summary:        Rust crate "pin-project-lite"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/pin-project-lite
#!RemoteAsset:  sha256:a89322df9ebe1c1578d689c92318e070967d1042b512afbe49518723f4e6d5cd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "pin-project-lite"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
