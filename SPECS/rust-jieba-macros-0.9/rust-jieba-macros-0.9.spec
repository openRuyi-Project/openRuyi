# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jieba-macros
%global full_version 0.9.0
%global pkgname jieba-macros-0.9

Name:           rust-jieba-macros-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "jieba-macros"
License:        MIT
URL:            https://github.com/messense/jieba-rs
#!RemoteAsset:  sha256:a29cfc5dcd898604c6f80363411fa6b6b08e27d1d253d6225b9cb6702ea02fc0
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
