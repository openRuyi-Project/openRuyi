# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerofrom-derive
%global full_version 0.1.7
%global pkgname zerofrom-derive-0.1

Name:           rust-zerofrom-derive-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "zerofrom-derive"
License:        Unicode-3.0
URL:            https://github.com/unicode-org/icu4x
#!RemoteAsset:  sha256:11532158c46691caf0f2593ea8358fed6bbf68a0315e80aae9bd41fbade684a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.61
Requires:       crate(quote-1/default) >= 1.0.44
Requires:       crate(syn-2/default) >= 2.0.21
Requires:       crate(syn-2/fold) >= 2.0.21
Requires:       crate(synstructure-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zerofrom-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
