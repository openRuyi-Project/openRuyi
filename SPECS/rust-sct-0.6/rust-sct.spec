# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sct
%global full_version 0.6.1
%global pkgname sct-0.6

Name:           rust-sct-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "sct"
License:        Apache-2.0/ISC/MIT
URL:            https://github.com/ctz/sct.rs
#!RemoteAsset:  sha256:b362b83898e0e69f38515b82ee15aa80636befe47c3b6d3d89a911e78fc228ce
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.16/default) >= 0.16.20
Requires:       crate(untrusted-0.7/default) >= 0.7.0
Provides:       crate(sct) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "sct"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
