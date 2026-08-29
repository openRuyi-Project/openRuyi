# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name landlock
%global full_version 0.4.5
%global pkgname landlock-0.4

Name:           rust-landlock-0.4
Version:        0.4.5
Release:        %autorelease
Summary:        Rust crate "landlock"
License:        MIT OR Apache-2.0
URL:            https://landlock.io
#!RemoteAsset:  sha256:635839550ae8b90d9fd2571460a6645dc0aec070225956ca7a2831ed31d2795d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(enumflags2-0.7/default) >= 0.7.0
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "landlock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
