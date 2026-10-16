# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ntest_test_cases
%global full_version 0.9.5
%global pkgname ntest-test-cases-0.9

Name:           rust-ntest-test-cases-0.9
Version:        0.9.5
Release:        %autorelease
Summary:        Rust crate "ntest_test_cases"
License:        MIT
URL:            https://github.com/becheran/ntest
#!RemoteAsset:  sha256:6913433c6319ef9b2df316bb8e3db864a41724c2bb8f12555e07dc4ec69d3db1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.0
Requires:       crate(syn-1/full) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ntest_test_cases"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
