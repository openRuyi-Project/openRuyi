# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name miow
%global full_version 0.2.2
%global pkgname miow-0.2

Name:           rust-miow-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "miow"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/miow
#!RemoteAsset:  sha256:ebd808424166322d4a38da87083bfddd3ac4c131334ed55856112eb06d46944d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(kernel32-sys-0.2/default) >= 0.2.0
Requires:       crate(net2-0.2) >= 0.2.36
Requires:       crate(winapi-0.2/default) >= 0.2.0
Requires:       crate(ws2-32-sys-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "miow"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
