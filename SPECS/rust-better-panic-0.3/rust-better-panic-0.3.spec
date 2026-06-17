# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name better-panic
%global full_version 0.3.0
%global pkgname better-panic-0.3

Name:           rust-better-panic-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "better-panic"
License:        MIT
URL:            https://github.com/mitsuhiko/better-panic
#!RemoteAsset:  sha256:6fa9e1d11a268684cbd90ed36370d7577afb6c62d912ddff5c15fc34343e5036
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(backtrace-0.3/default) >= 0.3.37
Requires:       crate(console-0.15) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "better-panic"

%package     -n %{name}+syntect
Summary:        Pretty panic backtraces inspired by Python's tracebacks - feature "syntect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syntect-4/default) >= 4.6.0
Provides:       crate(%{pkgname}/syntect) = %{version}

%description -n %{name}+syntect
This metapackage enables feature "syntect" for the Rust better-panic crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
