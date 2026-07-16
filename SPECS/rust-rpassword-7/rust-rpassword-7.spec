# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rpassword
%global full_version 7.4.0
%global pkgname rpassword-7

Name:           rust-rpassword-7
Version:        7.4.0
Release:        %autorelease
Summary:        Rust crate "rpassword"
License:        Apache-2.0
URL:            https://github.com/conradkleinespel/rpassword
#!RemoteAsset:  sha256:66d4c8b64f049c6721ec8ccec37ddfc3d641c4a7fca57e8f2a89de509c73df39
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(rtoolbox-0.0.3/default) >= 0.0.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rpassword"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
