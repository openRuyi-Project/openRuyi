# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jieba-macros
%global full_version 0.10.3
%global pkgname jieba-macros-0.10

Name:           rust-jieba-macros-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "jieba-macros"
License:        MIT
URL:            https://github.com/messense/jieba-rs
#!RemoteAsset:  sha256:34904340bc65749a9e9a02fcc7f3368e675427c18447b9bbe02df52c15c9a36a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-codegen-0.13/default) >= 0.13.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "jieba-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
