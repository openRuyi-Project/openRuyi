# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unty
%global full_version 0.0.4
%global pkgname unty-0.0.4

Name:           rust-unty-0.0.4
Version:        0.0.4
Release:        %autorelease
Summary:        Rust crate "unty"
License:        MIT OR Apache-2.0
URL:            https://github.com/bincode-org/unty
#!RemoteAsset:  sha256:6d49784317cd0d1ee7ec5c716dd598ec5b4483ea832a2dced265471cc0f690ae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "unty"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
