# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name basic-toml
%global full_version 0.1.10
%global pkgname basic-toml-0.1

Name:           rust-basic-toml-0.1
Version:        0.1.10
Release:        %autorelease
Summary:        Rust crate "basic-toml"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/basic-toml
#!RemoteAsset:  sha256:ba62675e8242a4c4e806d12f11d136e626e6c8361d6b829310732241652a178a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.194

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "basic-toml"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
