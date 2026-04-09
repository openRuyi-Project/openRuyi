# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name csv
%global full_version 1.4.0
%global pkgname csv-1.0

Name:           rust-csv-1.0
Version:        1.4.0
Release:        %autorelease
Summary:        Rust crate "csv"
License:        Unlicense/MIT
URL:            https://github.com/BurntSushi/rust-csv
#!RemoteAsset:  sha256:52cd9d68cf7efc6ddfaaee42e7288d3a99d613d4b50f76ce9827ae0c6e14f938
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(csv-core-0.1/default) >= 0.1.11
Requires:       crate(itoa-1.0/default) >= 1.0.0
Requires:       crate(ryu-1.0/default) >= 1.0.0
Requires:       crate(serde-core-1.0/default) >= 1.0.221
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "csv"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
