# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name which
%global full_version 2.0.1
%global pkgname which-2

Name:           rust-which-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "which"
License:        MIT
URL:            https://github.com/harryfei/which-rs.git
#!RemoteAsset:  sha256:b57acb10231b9493c8472b20cb57317d0679a49e0bdbee44b3b803a6473af164
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(failure-0.1/std) >= 0.1.1
Requires:       crate(libc-0.2/default) >= 0.2.10

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Locate installed execuable in cross platforms.
Source code for takopackized Rust crate "which"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
