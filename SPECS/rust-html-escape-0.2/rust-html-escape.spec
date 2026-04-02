# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name html-escape
%global full_version 0.2.13
%global pkgname html-escape-0.2

Name:           rust-html-escape-0.2
Version:        0.2.13
Release:        %autorelease
Summary:        Rust crate "html-escape"
License:        MIT
URL:            https://magiclen.org/html-escape
#!RemoteAsset:  sha256:6d1ad449764d627e22bfd7cd5e8868264fc9236e07c752972b4080cd351cb476
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(utf8-width-0.1/default) >= 0.1.8
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "html-escape"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
