# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unsafe-libyaml-norway
%global full_version 0.2.13
%global pkgname unsafe-libyaml-norway-0.2

Name:           rust-unsafe-libyaml-norway-0.2
Version:        0.2.13
Release:        %autorelease
Summary:        Rust crate "unsafe-libyaml-norway"
License:        MIT
URL:            https://github.com/cafkafk/unsafe-libyaml-norway
#!RemoteAsset:  sha256:6725b6489a7cc8867248a694a4a8b7620ecf9dd11ecfc17a77943bf155b11d29
Source:         https://static.crates.io/crates/unsafe-libyaml-norway/0.2.13/download#/rust-unsafe-libyaml-norway-0.2-0.2.13.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "unsafe-libyaml-norway"

%package     -n %{name}+default
Summary:        Libyaml transpiled to rust by c2rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust unsafe-libyaml-norway crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
