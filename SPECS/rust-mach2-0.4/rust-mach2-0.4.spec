# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mach2
%global full_version 0.4.3
%global pkgname mach2-0.4

Name:           rust-mach2-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "mach2"
License:        BSD-2-Clause OR MIT OR Apache-2.0
URL:            https://github.com/JohnTitor/mach2
#!RemoteAsset:  sha256:d640282b302c0bb0a2a8e0233ead9035e3bed871f0b7e81fe4a1ec829765db44
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "mach2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
