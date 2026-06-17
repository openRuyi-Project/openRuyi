# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-crate
%global full_version 3.5.0
%global pkgname proc-macro-crate-3

Name:           rust-proc-macro-crate-3
Version:        3.5.0
Release:        %autorelease
Summary:        Rust crate "proc-macro-crate"
License:        MIT OR Apache-2.0
URL:            https://github.com/bkchr/proc-macro-crate
#!RemoteAsset:  sha256:e67ba7e9b2b56446f1d419b1d807906278ffa1a658a8a5d8a39dcb1f5a78614f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(toml-edit-0.25/parse) >= 0.25.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro-crate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
