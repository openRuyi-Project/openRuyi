# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name enum-as-inner
%global full_version 0.6.1
%global pkgname enum-as-inner-0.6

Name:           rust-enum-as-inner-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "enum-as-inner"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluejekyll/enum-as-inner
#!RemoteAsset:  sha256:a1e6a265c649f3f5979b601d26f1d05ada116434c87741c9493cb56218f76cbc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "enum-as-inner"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
