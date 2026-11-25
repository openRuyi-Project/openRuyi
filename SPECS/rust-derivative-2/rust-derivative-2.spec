# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derivative
%global full_version 2.2.0
%global pkgname derivative-2

Name:           rust-derivative-2
Version:        2.2.0
Release:        %autorelease
Summary:        Rust crate "derivative"
License:        MIT OR Apache-2.0
URL:            https://github.com/mcarton/rust-derivative
#!RemoteAsset:  sha256:fcc3dd5e9e9c0b295d6e1e4d811fb6f157d5ffd784b8d202fc62eac8035a770b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-1/default) >= 1.0.3
Requires:       crate(syn-1/extra-traits) >= 1.0.3
Requires:       crate(syn-1/visit) >= 1.0.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-core) = %{version}

%description
Source code for takopackized Rust crate "derivative"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
