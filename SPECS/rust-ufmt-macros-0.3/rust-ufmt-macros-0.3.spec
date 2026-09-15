# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ufmt-macros
%global full_version 0.3.0
%global pkgname ufmt-macros-0.3

Name:           rust-ufmt-macros-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "ufmt-macros"
License:        MIT OR Apache-2.0
URL:            https://github.com/japaric/ufmt
#!RemoteAsset:  sha256:d337d3be617449165cb4633c8dece429afd83f84051024079f97ad32a9663716
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
Source code for the Rust crate "ufmt-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
