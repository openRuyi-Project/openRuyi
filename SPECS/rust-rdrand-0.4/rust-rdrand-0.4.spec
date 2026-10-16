# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rdrand
%global full_version 0.4.0
%global pkgname rdrand-0.4

Name:           rust-rdrand-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "rdrand"
License:        ISC
URL:            https://github.com/nagisa/rust_rdrand/
#!RemoteAsset:  sha256:678054eb77286b51581ba43620cc911abf02758c91f93f479767aed0f90458b2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.3) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "rdrand"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
