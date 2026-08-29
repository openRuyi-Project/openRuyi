# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name indenter
%global full_version 0.3.4
%global pkgname indenter-0.3

Name:           rust-indenter-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "indenter"
License:        MIT OR Apache-2.0
URL:            https://github.com/yaahc/indenter
#!RemoteAsset:  sha256:964de6e86d545b246d84badc0fef527924ace5134f30641c203ef52ba83f58d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "indenter"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
