# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name simplecss
%global full_version 0.2.2
%global pkgname simplecss-0.2

Name:           rust-simplecss-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "simplecss"
License:        Apache-2.0 OR MIT
URL:            https://github.com/linebender/simplecss
#!RemoteAsset:  sha256:7a9c6883ca9c3c7c90e888de77b7a5c849c779d25d74a1269b0218b14e8b136c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4) >= 0.4.22

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "simplecss"

%package     -n %{name}+std
Summary:        Simple CSS 2 parser and selector - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/std) >= 0.4.22
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust simplecss crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
