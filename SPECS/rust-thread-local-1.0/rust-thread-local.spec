# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread_local
%global full_version 1.1.9
%global pkgname thread-local-1.0

Name:           rust-thread-local-1.0
Version:        1.1.9
Release:        %autorelease
Summary:        Rust crate "thread_local"
License:        MIT OR Apache-2.0
URL:            https://github.com/Amanieu/thread_local-rs
#!RemoteAsset:  sha256:f60246a4944f24f6e018aa17cdeffb7818b76356965d03b07d6a9886e8962185
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "thread_local"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
