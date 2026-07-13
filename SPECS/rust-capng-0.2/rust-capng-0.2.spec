# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name capng
%global full_version 0.2.2
%global pkgname capng-0.2

Name:           rust-capng-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "capng"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/slp/capng
#!RemoteAsset:  sha256:f6f8e9448233603643e42606121d95f5f8d4e015b3e7619a51593864dd902575
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.69

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "capng"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
