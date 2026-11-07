# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name failure_derive
%global full_version 0.1.8
%global pkgname failure-derive-0.1

Name:           rust-failure-derive-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "failure_derive"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/failure/
#!RemoteAsset:  sha256:aa4da3c766cd7a0db8242e326e9e4e081edd567072893ed320008189715366a4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.3
Requires:       crate(synstructure-0.12/default) >= 0.12.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "failure_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
