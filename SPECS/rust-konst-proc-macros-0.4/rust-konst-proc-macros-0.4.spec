# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name konst_proc_macros
%global full_version 0.4.1
%global pkgname konst-proc-macros-0.4

Name:           rust-konst-proc-macros-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "konst_proc_macros"
License:        Zlib
URL:            https://github.com/rodrimati1992/konst/
#!RemoteAsset:  sha256:e037a2e1d8d5fdbd49b16a4ea09d5d6401c1f29eca5ff29d03d3824dba16256a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "konst_proc_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
