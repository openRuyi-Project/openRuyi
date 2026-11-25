# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name getset
%global full_version 0.1.7
%global pkgname getset-0.1

Name:           rust-getset-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "getset"
License:        MIT
URL:            https://github.com/jbaublitz/getset
#!RemoteAsset:  sha256:6cf442baaabe4213ce7d1239afc26c039180b6456da2cededa316ae2c8a77a77
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
A procedural macro for generating the most basic getters and setters on fields.
Source code for takopackized Rust crate "getset"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
