# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-normalization-alignments
%global full_version 0.1.12
%global pkgname unicode-normalization-alignments-0.1

Name:           rust-unicode-normalization-alignments-0.1
Version:        0.1.12
Release:        %autorelease
Summary:        Rust crate "unicode-normalization-alignments"
License:        MIT OR Apache-2.0
URL:            https://github.com/n1t0/unicode-normalization
#!RemoteAsset:  sha256:43f613e4fa046e69818dd287fdc4bc78175ff20331479dab6e1b0f98d57062de
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1.0/default) >= 1.15.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "unicode-normalization-alignments"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
