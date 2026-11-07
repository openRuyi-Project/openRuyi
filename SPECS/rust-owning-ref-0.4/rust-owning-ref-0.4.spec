# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name owning_ref
%global full_version 0.4.1
%global pkgname owning-ref-0.4

Name:           rust-owning-ref-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "owning_ref"
License:        MIT
URL:            https://github.com/Kimundi/owning-ref-rs
#!RemoteAsset:  sha256:6ff55baddef9e4ad00f88b6c743a2a8062d4c6ade126c2a528644b8e444d52ce
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(stable-deref-trait-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "owning_ref"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
