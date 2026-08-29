# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libc-print
%global full_version 0.3.0
%global pkgname libc-print-0.3

Name:           rust-libc-print-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "libc-print"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/rust-libc-print
#!RemoteAsset:  sha256:6e4fb34ccfede7d939c50cf24b65e228fa2af1d3b49f6efd44b080dd3dcf2f1e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.186
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libc-print"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
