# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name instability
%global full_version 0.3.12
%global pkgname instability-0.3

Name:           rust-instability-0.3
Version:        0.3.12
Release:        %autorelease
Summary:        Rust crate "instability"
License:        MIT
URL:            https://github.com/ratatui/instability
#!RemoteAsset:  sha256:5eb2d60ef19920a3a9193c3e371f726ec1dafc045dac788d0fb3704272458971
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.23/default) >= 0.23.0
Requires:       crate(indoc-2/default) >= 2.0.0
Requires:       crate(proc-macro2-1/default) >= 1.0.86
Requires:       crate(quote-1/default) >= 1.0.25
Requires:       crate(syn-2/default) >= 2.0.15
Requires:       crate(syn-2/derive) >= 2.0.15
Requires:       crate(syn-2/full) >= 2.0.15
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
A fork of the `stability` crate.
Source code for takopackized Rust crate "instability"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
