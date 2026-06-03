# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rayon-cond
%global full_version 0.4.0
%global pkgname rayon-cond-0.4

Name:           rust-rayon-cond-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "rayon-cond"
License:        Apache-2.0 OR MIT
URL:            https://github.com/cuviper/rayon-cond
#!RemoteAsset:  sha256:2964d0cf57a3e7a06e8183d14a8b527195c706b7983549cd5462d5aa3747438f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1.0/default) >= 1.15.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(rayon-1.0/default) >= 1.11.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rayon-cond"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
