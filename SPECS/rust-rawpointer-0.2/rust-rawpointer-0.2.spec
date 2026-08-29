# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rawpointer
%global full_version 0.2.1
%global pkgname rawpointer-0.2

Name:           rust-rawpointer-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "rawpointer"
License:        MIT OR Apache-2.0
URL:            https://github.com/bluss/rawpointer/
#!RemoteAsset:  sha256:60a357793950651c4ed0f3f52338f53b2f809f32d83a07f72909fa13e4c6c1e3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
For example `.post_inc()` and `.pre_dec()` (c.f. `ptr++` and `--ptr`), `offset` and `add` for `NonNull<T>`, and the function `ptrdistance`.
Source code for takopackized Rust crate "rawpointer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
