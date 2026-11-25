# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name replace_with
%global full_version 0.1.8
%global pkgname replace-with-0.1

Name:           rust-replace-with-0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Rust crate "replace_with"
License:        MIT OR Apache-2.0
URL:            https://github.com/alecmocatta/replace_with
#!RemoteAsset:  sha256:51743d3e274e2b18df81c4dc6caf8a5b8e15dbe799e0dca05c7617380094e884
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/panic-abort) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "replace_with"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
