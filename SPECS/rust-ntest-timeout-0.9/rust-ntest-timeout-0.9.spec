# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ntest_timeout
%global full_version 0.9.5
%global pkgname ntest-timeout-0.9

Name:           rust-ntest-timeout-0.9
Version:        0.9.5
Release:        %autorelease
Summary:        Rust crate "ntest_timeout"
License:        MIT
URL:            https://github.com/becheran/ntest
#!RemoteAsset:  sha256:9224be3459a0c1d6e9b0f42ab0e76e98b29aef5aba33c0487dfcf47ea08b5150
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro-crate-1/default) >= 1.1.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0
Requires:       crate(syn-1/full) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ntest_timeout"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
