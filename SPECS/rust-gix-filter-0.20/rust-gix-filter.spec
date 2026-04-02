# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-filter
%global full_version 0.20.0
%global pkgname gix-filter-0.20

Name:           rust-gix-filter-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "gix-filter"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:aa6571a3927e7ab10f64279a088e0dae08e8da05547771796d7389bbe28ad9ff
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(encoding-rs-0.8/default) >= 0.8.35
Requires:       crate(gix-attributes-0.27/default) >= 0.27.0
Requires:       crate(gix-command-0.6/default) >= 0.6.5
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-packetline-blocking-0.19/default) >= 0.19.3
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-quote-0.6/default) >= 0.6.2
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-filter"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
