# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name oorandom
%global full_version 11.1.5
%global pkgname oorandom-11.0

Name:           rust-oorandom-11.0
Version:        11.1.5
Release:        %autorelease
Summary:        Rust crate "oorandom"
License:        MIT
URL:            https://hg.sr.ht/~icefox/oorandom
#!RemoteAsset:  sha256:d6790f58c7ff633d8771f42965289203411a5e5c68388703c06e14f24770b41e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "oorandom"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
