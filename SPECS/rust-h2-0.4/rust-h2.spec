# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name h2
%global full_version 0.4.13
%global pkgname h2-0.4

Name:           rust-h2-0.4
Version:        0.4.13
Release:        %autorelease
Summary:        Rust crate "h2"
License:        MIT
URL:            https://github.com/hyperium/h2
#!RemoteAsset:  sha256:2f44da3a8150a6703ed5d34e164b875fd14c2cdab9af1252a9a1020bde2bdc54
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atomic-waker-1.0/default) >= 1.1.2
Requires:       crate(bytes-1.0/default) >= 1.11.1
Requires:       crate(fnv-1.0/default) >= 1.0.7
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-sink-0.3) >= 0.3.32
Requires:       crate(http-1.0/default) >= 1.4.0
Requires:       crate(indexmap-2.0/default) >= 2.13.0
Requires:       crate(indexmap-2.0/std) >= 2.13.0
Requires:       crate(slab-0.4/default) >= 0.4.12
Requires:       crate(tokio-1.0/default) >= 1.50.0
Requires:       crate(tokio-1.0/io-util) >= 1.50.0
Requires:       crate(tokio-util-0.7/codec) >= 0.7.18
Requires:       crate(tokio-util-0.7/default) >= 0.7.18
Requires:       crate(tokio-util-0.7/io) >= 0.7.18
Requires:       crate(tracing-0.1/std) >= 0.1.44
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/stream)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "h2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
