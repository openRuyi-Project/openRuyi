# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name macrotest
%global full_version 1.2.1
%global pkgname macrotest-1

Name:           rust-macrotest-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "macrotest"
License:        MIT OR Apache-2.0
URL:            https://github.com/eupn/macrotest
#!RemoteAsset:  sha256:cd198afd908012e57564b66e43e7d4d19056cec7e6232e9e6d54a1798622f81d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(diff-0.1/default) >= 0.1.0
Requires:       crate(fastrand-2/default) >= 2.0.0
Requires:       crate(glob-0.3/default) >= 0.3.0
Requires:       crate(prettyplease-0.2/default) >= 0.2.0
Requires:       crate(serde-1/default) >= 1.0.105
Requires:       crate(serde-derive-1/default) >= 1.0.105
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(toml-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "macrotest"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
