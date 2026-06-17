# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cexpr
%global full_version 0.6.0
%global pkgname cexpr-0.6

Name:           rust-cexpr-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "cexpr"
License:        Apache-2.0 OR MIT
URL:            https://github.com/jethrogb/rust-cexpr
#!RemoteAsset:  sha256:6fac387a98bb7c37292057cffc56d62ecb629900026402633ae9160df93a8766
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(nom-7/std) >= 7.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cexpr"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
