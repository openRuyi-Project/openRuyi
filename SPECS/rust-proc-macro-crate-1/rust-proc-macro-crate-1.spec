# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-crate
%global full_version 1.3.1
%global pkgname proc-macro-crate-1

Name:           rust-proc-macro-crate-1
Version:        1.3.1
Release:        %autorelease
Summary:        Rust crate "proc-macro-crate"
License:        MIT OR Apache-2.0
URL:            https://github.com/bkchr/proc-macro-crate
#!RemoteAsset:  sha256:7f4c021e1093a56626774e81216a4ce732a735e5bad4868a03f3ed65ca0c3919
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.13.0
Requires:       crate(toml-edit-0.19/default) >= 0.19.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-crate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
