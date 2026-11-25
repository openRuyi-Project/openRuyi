# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lockfile
%global full_version 0.4.0
%global pkgname lockfile-0.4

Name:           rust-lockfile-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "lockfile"
License:        MIT OR Apache-2.0 OR ISC
URL:            https://github.com/derekdreery/lockfile-rs
#!RemoteAsset:  sha256:5be1cf190319c74ba3e45923624626ae2e43fe42ad7e60ff38ded81044c37630
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "lockfile"

%package     -n %{name}+log
Summary:        Create lockfiles that remove themselves when they are dropped - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.17
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust lockfile crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
