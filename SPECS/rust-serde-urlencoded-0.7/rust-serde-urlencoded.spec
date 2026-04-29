# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_urlencoded
%global full_version 0.7.1
%global pkgname serde-urlencoded-0.7

Name:           rust-serde-urlencoded-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "serde_urlencoded"
License:        MIT/Apache-2.0
URL:            https://github.com/nox/serde_urlencoded
#!RemoteAsset:  sha256:d3491c14715ca2294c4d6a88f15e84739788c1d030eed8c110436aafdaa2f3fd
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(form-urlencoded-1.0/default) >= 1.2.2
Requires:       crate(itoa-1.0/default) >= 1.0.18
Requires:       crate(ryu-1.0/default) >= 1.0.23
Requires:       crate(serde-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "serde_urlencoded"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
