# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cfb
%global full_version 0.14.0
%global pkgname cfb-0.14

Name:           rust-cfb-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "cfb"
License:        MIT
URL:            https://github.com/mdsteele/rust-cfb
#!RemoteAsset:  sha256:a347dcabdae9c31b0825fd6a8bed285ec9c2acb89c47827126d52fa4f59cece3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.0
Requires:       crate(uuid-1/default) >= 1.0.0
Requires:       crate(web-time-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cfb"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
