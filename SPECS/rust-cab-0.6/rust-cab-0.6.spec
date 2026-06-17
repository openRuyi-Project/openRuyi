# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cab
%global full_version 0.6.0
%global pkgname cab-0.6

Name:           rust-cab-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "cab"
License:        MIT
URL:            https://github.com/mdsteele/rust-cab
#!RemoteAsset:  sha256:171228650e6721d5acc0868a462cd864f49ac5f64e4a42cde270406e64e404d2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.0.0
Requires:       crate(flate2-1/rust-backend) >= 1.0.0
Requires:       crate(lzxd-0.2/default) >= 0.2.5
Requires:       crate(time-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cab"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
