# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ct-codecs
%global full_version 1.1.6
%global pkgname ct-codecs-1.0

Name:           rust-ct-codecs-1.0
Version:        1.1.6
Release:        %autorelease
Summary:        Rust crate "ct-codecs"
License:        MIT
URL:            https://github.com/jedisct1/rust-ct-codecs
#!RemoteAsset:  sha256:9b10589d1a5e400d61f9f38f12f884cfd080ff345de8f17efda36fe0e4a02aa8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "ct-codecs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
