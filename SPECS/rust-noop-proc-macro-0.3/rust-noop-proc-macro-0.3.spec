# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name noop_proc_macro
%global full_version 0.3.0
%global pkgname noop-proc-macro-0.3

Name:           rust-noop-proc-macro-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "noop_proc_macro"
License:        MIT
URL:            https://github.com/lu-zero/noop_proc_macro
#!RemoteAsset:  sha256:0676bb32a98c1a483ce53e500a81ad9c3d5b3f7c920c28c24e9cb0980d0b5bc8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "noop_proc_macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
