# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name utf8-width
%global full_version 0.1.8
%global pkgname utf8-width-0.1

Name:           rust-utf8-width-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "utf8-width"
License:        MIT
URL:            https://magiclen.org/utf8-width
#!RemoteAsset:  sha256:1292c0d970b54115d14f2492fe0170adf21d68a1de108eebc51c1df4f346a091
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "utf8-width"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
