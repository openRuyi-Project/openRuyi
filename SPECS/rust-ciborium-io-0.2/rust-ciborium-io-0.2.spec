# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ciborium-io
%global full_version 0.2.2
%global pkgname ciborium-io-0.2

Name:           rust-ciborium-io-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "ciborium-io"
License:        Apache-2.0
URL:            https://github.com/enarx/ciborium
#!RemoteAsset:  sha256:05afea1e0a06c9be33d539b876f1ce3692f4afea2cb41f740e7743225ed1c757
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "ciborium-io"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
