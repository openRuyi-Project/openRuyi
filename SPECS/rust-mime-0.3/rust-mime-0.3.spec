# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mime
%global full_version 0.3.17
%global pkgname mime-0.3

Name:           rust-mime-0.3
Version:        0.3.17
Release:        %autorelease
Summary:        Rust crate "mime"
License:        MIT OR Apache-2.0
URL:            https://github.com/hyperium/mime
#!RemoteAsset:  sha256:6877bb514081ee2a7ff5ef9de3281f14a4dd4bceac4c09388074a6b5df8a139a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mime"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
