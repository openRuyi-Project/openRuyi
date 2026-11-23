# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rstest_reuse
%global full_version 0.7.2
%global pkgname rstest-reuse-0.7

Name:           rust-rstest-reuse-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "rstest_reuse"
License:        MIT OR Apache-2.0
URL:            https://github.com/la10736/rstest
#!RemoteAsset:  sha256:8ef60cf9121b65330c7c844c94ad66b7d912e98b2ba07cb61ef4fd0dfa7042e2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1/default) >= 1.0.37
Requires:       crate(rand-0.8/default) >= 0.8.5
Requires:       crate(syn-3/default) >= 3.0.8
Requires:       crate(syn-3/extra-traits) >= 3.0.8
Requires:       crate(syn-3/full) >= 3.0.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rstest_reuse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
