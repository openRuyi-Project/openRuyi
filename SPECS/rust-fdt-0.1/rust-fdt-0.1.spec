# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fdt
%global full_version 0.1.5
%global pkgname fdt-0.1

Name:           rust-fdt-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "fdt"
License:        MPL-2.0
URL:            https://github.com/repnop/fdt
#!RemoteAsset:  sha256:784a4df722dc6267a04af36895398f59d21d07dce47232adf31ec0ff2fa45e67
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/pretty-printing) = %{version}

%description
Source code for takopackized Rust crate "fdt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
