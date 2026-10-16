# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fuchsia-cprng
%global full_version 0.1.1
%global pkgname fuchsia-cprng-0.1

Name:           rust-fuchsia-cprng-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "fuchsia-cprng"
License:        FIXME
URL:            https://fuchsia.googlesource.com/fuchsia/+/master/garnet/public/rust/fuchsia-cprng
#!RemoteAsset:  sha256:a06f77d526c1a601b7c4cdd98f54b5eaabffc14d5f2f0296febdc7f357c6d3ba
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fuchsia-cprng"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
