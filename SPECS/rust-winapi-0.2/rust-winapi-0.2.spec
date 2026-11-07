# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winapi
%global full_version 0.2.8
%global pkgname winapi-0.2

Name:           rust-winapi-0.2
Version:        0.2.8
Release:        %autorelease
Summary:        Rust crate "winapi"
License:        MIT
URL:            https://github.com/retep998/winapi-rs
#!RemoteAsset:  sha256:167dc9d6949a9b857f3451275e911c3f44255842c1f7a76f33c55103a909087a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
See README for list of crates providing function bindings.
Source code for takopackized Rust crate "winapi"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
