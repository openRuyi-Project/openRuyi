# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name io-uring
%global full_version 0.7.8
%global pkgname io-uring-0.7

Name:           rust-io-uring-0.7
Version:        0.7.8
Release:        %autorelease
Summary:        Rust crate "io-uring"
License:        MIT OR Apache-2.0
URL:            https://github.com/tokio-rs/io-uring
#!RemoteAsset:  sha256:b86e202f00093dcba4275d4636b93ef9dd75d025ae560d2521b45ea28ab49013
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.9.1
Requires:       crate(cfg-if-1.0/default) >= 1.0.1
Requires:       crate(libc-0.2) >= 0.2.174
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/io-safety)

%description
Source code for takopackized Rust crate "io-uring"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
