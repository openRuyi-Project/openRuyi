# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arwen-codesign
%global full_version 0.0.1-alpha.1
%global pkgname arwen-codesign-0.0.1-alpha.1

Name:           rust-arwen-codesign-0.0.1-alpha.1
Version:        0.0.1
Release:        %autorelease
Summary:        Rust crate "arwen-codesign"
License:        MIT
URL:            https://github.com/nichmor/arwen
#!RemoteAsset:  sha256:35d7a19757bfe3658d5a95bf25a0492f29ebb21933549bdbfa4075c895510124
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(goblin-0.10/default) >= 0.10.4
Requires:       crate(goblin-0.10/mach64) >= 0.10.4
Requires:       crate(scroll-0.13/default) >= 0.13.0
Requires:       crate(sha2-0.10/default) >= 0.10.0
Requires:       crate(tempfile-3/default) >= 3.16.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arwen-codesign"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
