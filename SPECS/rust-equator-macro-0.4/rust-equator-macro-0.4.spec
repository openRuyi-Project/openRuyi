# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name equator-macro
%global full_version 0.4.2
%global pkgname equator-macro-0.4

Name:           rust-equator-macro-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "equator-macro"
License:        MIT
URL:            https://github.com/sarah-ek/equator/
#!RemoteAsset:  sha256:44f23cf4b44bfce11a86ace86f8a73ffdec849c9fd00a386a53d278bd9e81fb3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.86
Requires:       crate(quote-1/default) >= 1.0.36
Requires:       crate(syn-2/default) >= 2.0.72
Requires:       crate(syn-2/full) >= 2.0.72
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "equator-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
