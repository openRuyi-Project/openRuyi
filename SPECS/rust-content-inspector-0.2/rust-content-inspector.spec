# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name content_inspector
%global full_version 0.2.4
%global pkgname content-inspector-0.2

Name:           rust-content-inspector-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "content_inspector"
License:        MIT/Apache-2.0
URL:            https://github.com/sharkdp/content_inspector
#!RemoteAsset:  sha256:b7bda66e858c683005a53a9a60c69a4aca7eeaa45d124526e389f7aec8e62f38
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2.0/default) >= 2.8.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "content_inspector"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
