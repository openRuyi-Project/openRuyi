# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pin-project
%global full_version 1.1.10
%global pkgname pin-project-1

Name:           rust-pin-project-1
Version:        1.1.10
Release:        %autorelease
Summary:        Rust crate "pin-project"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/pin-project
#!RemoteAsset:  sha256:677f1add503faace112b9f1373e43e9e054bfdd22ff1a63c1bc485eaec6a6a8a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-internal-1/default) >= 1.1.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pin-project"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
