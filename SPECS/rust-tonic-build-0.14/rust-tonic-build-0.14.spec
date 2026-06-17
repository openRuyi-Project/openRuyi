# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic-build
%global full_version 0.14.2
%global pkgname tonic-build-0.14

Name:           rust-tonic-build-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "tonic-build"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:4c40aaccc9f9eccf2cd82ebc111adc13030d23e887244bc9cfa5d1d636049de3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(prettyplease-0.2/default) >= 0.2.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/transport) = %{version}

%description
Source code for takopackized Rust crate "tonic-build"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
