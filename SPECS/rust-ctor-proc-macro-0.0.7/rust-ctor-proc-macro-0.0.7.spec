# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ctor-proc-macro
%global full_version 0.0.7
%global pkgname ctor-proc-macro-0.0.7

Name:           rust-ctor-proc-macro-0.0.7
Version:        0.0.7
Release:        %autorelease
Summary:        Rust crate "ctor-proc-macro"
License:        Apache-2.0 OR MIT
URL:            https://github.com/mmastrac/rust-ctor
#!RemoteAsset:  sha256:52560adf09603e58c9a7ee1fe1dcb95a16927b17c127f0ac02d6e768a0e25bc1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ctor-proc-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
