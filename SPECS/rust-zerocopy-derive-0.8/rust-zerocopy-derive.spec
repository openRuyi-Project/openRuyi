# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy-derive
%global full_version 0.8.48
%global pkgname zerocopy-derive-0.8

Name:           rust-zerocopy-derive-0.8
Version:        0.8.48
Release:        %autorelease
Summary:        Rust crate "zerocopy-derive"
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:70e3cd084b1788766f53af483dd21f93881ff30d7320490ec3ef7526d203bad4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "zerocopy-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
