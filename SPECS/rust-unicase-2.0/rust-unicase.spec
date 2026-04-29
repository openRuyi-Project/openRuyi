# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicase
%global full_version 2.9.0
%global pkgname unicase-2.0

Name:           rust-unicase-2.0
Version:        2.9.0
Release:        %autorelease
Summary:        Rust crate "unicase"
License:        MIT OR Apache-2.0
URL:            https://github.com/seanmonstar/unicase
#!RemoteAsset:  sha256:dbc4bc3a9f746d862c45cb89d705aa10f187bb96c76001afab07a0d35ce60142
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "unicase"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
