# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cvt
%global full_version 0.1.2
%global pkgname cvt-0.1

Name:           rust-cvt-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "cvt"
License:        Apache-2.0
URL:            https://github.com/marmistrz/cvt
#!RemoteAsset:  sha256:d2ae9bf77fbf2d39ef573205d554d87e86c12f1994e9ea335b0651b9b278bcf1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cvt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
