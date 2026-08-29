# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name supports-unicode
%global full_version 2.1.0
%global pkgname supports-unicode-2

Name:           rust-supports-unicode-2
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "supports-unicode"
License:        Apache-2.0
URL:            https://github.com/zkat/supports-unicode
#!RemoteAsset:  sha256:f850c19edd184a205e883199a261ed44471c81e39bd95b1357f5febbef00e77a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(is-terminal-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "supports-unicode"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
