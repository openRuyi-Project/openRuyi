# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustfix
%global full_version 0.4.6
%global pkgname rustfix-0.4

Name:           rust-rustfix-0.4
Version:        0.4.6
Release:        %autorelease
Summary:        Rust crate "rustfix"
License:        Apache-2.0 OR MIT
URL:            https://github.com/rust-lang-nursery/rustfix
#!RemoteAsset:  sha256:7150ac777a2931a53489f5a41eb0937b84e3092a20cd0e73ad436b65b507f607
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(failure-0.1/default) >= 0.1.2
Requires:       crate(log-0.4/default) >= 0.4.1
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustfix"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
