# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name md5
%global full_version 0.8.1
%global pkgname md5-0.8

Name:           rust-md5-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "md5"
License:        Apache-2.0 OR MIT
URL:            https://github.com/stainless-steel/md5
#!RemoteAsset:  sha256:7ebb8d8732c6a6df3d8f032a82911cfc747e00efb95cc46e8d0acd5b5b88570c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "md5"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
