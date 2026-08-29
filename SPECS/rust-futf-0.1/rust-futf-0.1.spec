# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futf
%global full_version 0.1.5
%global pkgname futf-0.1

Name:           rust-futf-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "futf"
License:        MIT  OR  Apache-2.0
URL:            https://github.com/servo/futf
#!RemoteAsset:  sha256:df420e2e84819663797d1ec6544b13c5be84629e7bb00dc960d6917db2987843
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(mac-0.1/default) >= 0.1.0
Requires:       crate(new-debug-unreachable-1/default) >= 1.0.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "futf"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
