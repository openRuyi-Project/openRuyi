# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding
%global full_version 0.2.33
%global pkgname encoding-0.2

Name:           rust-encoding-0.2
Version:        0.2.33
Release:        %autorelease
Summary:        Rust crate "encoding"
License:        MIT
URL:            https://github.com/lifthrasiir/rust-encoding
#!RemoteAsset:  sha256:6b0d943856b990d12d3b55b359144ff341533e516d94098b1d3fc1ac666d36ec
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encoding-index-japanese-1/default) >= 1.20141219.5
Requires:       crate(encoding-index-korean-1/default) >= 1.20141219.5
Requires:       crate(encoding-index-simpchinese-1/default) >= 1.20141219.5
Requires:       crate(encoding-index-singlebyte-1/default) >= 1.20141219.5
Requires:       crate(encoding-index-tradchinese-1/default) >= 1.20141219.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "encoding"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
