# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name concat-string
%global full_version 1.0.1
%global pkgname concat-string-1

Name:           rust-concat-string-1
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "concat-string"
License:        Apache-2.0 OR MIT
URL:            https://github.com/FaultyRAM/concat-string
#!RemoteAsset:  sha256:7439becb5fafc780b6f4de382b1a7a3e70234afe783854a4702ee8adbb838609
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "concat-string"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
