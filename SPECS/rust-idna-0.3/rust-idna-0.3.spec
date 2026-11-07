# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name idna
%global full_version 0.3.0
%global pkgname idna-0.3

Name:           rust-idna-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "idna"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url/
#!RemoteAsset:  sha256:e14ddfc70884202db2244c223200c204c2bda1bc6e0998d11b5e024d657209e6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-bidi-0.3/default) >= 0.3.0
Requires:       crate(unicode-normalization-0.1/default) >= 0.1.17

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "idna"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
