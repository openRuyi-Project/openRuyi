# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thread_local
%global full_version 0.2.7
%global pkgname thread-local-0.2

Name:           rust-thread-local-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "thread_local"
License:        Apache-2.0 OR MIT
URL:            https://github.com/Amanieu/thread_local-rs
#!RemoteAsset:  sha256:8576dbbfcaef9641452d5cf0df9b0e7eeab7694956dd33bb61515fb8f18cfdd5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thread-id-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "thread_local"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
