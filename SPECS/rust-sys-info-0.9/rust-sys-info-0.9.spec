# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sys-info
%global full_version 0.9.1
%global pkgname sys-info-0.9

Name:           rust-sys-info-0.9
Version:        0.9.1
Release:        %autorelease
Summary:        Rust crate "sys-info"
License:        MIT
URL:            https://github.com/FillZpp/sys-info-rs
#!RemoteAsset:  sha256:0b3a0d0aba8bf96a0e1ddfdc352fc53b3df7f39318c71854910c3c4b024ae52c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.29

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
For now it supports Linux, Mac OS X, illumos, Solaris, FreeBSD, OpenBSD, and Windows.
Source code for takopackized Rust crate "sys-info"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
