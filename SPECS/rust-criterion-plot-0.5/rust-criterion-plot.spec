# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name criterion-plot
%global full_version 0.5.0
%global pkgname criterion-plot-0.5

Name:           rust-criterion-plot-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "criterion-plot"
License:        MIT/Apache-2.0
URL:            https://github.com/bheisler/criterion.rs
#!RemoteAsset:  sha256:6b50826342786a51a89e2da3a28f1c32b06e387201bc2d19791f622c673706b1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(itertools-0.10/default) >= 0.10.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "criterion-plot"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
