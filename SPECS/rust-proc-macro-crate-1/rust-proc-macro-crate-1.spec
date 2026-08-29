# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-crate
%global full_version 1.0.0
%global pkgname proc-macro-crate-1

Name:           rust-proc-macro-crate-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "proc-macro-crate"
License:        Apache-2.0 OR MIT
URL:            https://github.com/bkchr/proc-macro-crate
#!RemoteAsset:  sha256:41fdbd1df62156fbc5945f4762632564d7d038153091c3fcf1067f6aef7cff92
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thiserror-1/default) >= 1.0.24
Requires:       crate(toml-0.5/default) >= 0.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-crate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
