# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name radium
%global full_version 0.7.0
%global pkgname radium-0.7

Name:           rust-radium-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "radium"
License:        MIT
URL:            https://github.com/bitvecto-rs/radium
#!RemoteAsset:  sha256:dc33ff2d4973d518d823d61aa239014831e521c75da58e3df4840d3f47749d09
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "radium"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
