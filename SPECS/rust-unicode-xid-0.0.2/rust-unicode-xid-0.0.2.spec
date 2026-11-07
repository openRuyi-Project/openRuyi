# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-xid
%global full_version 0.0.2
%global pkgname unicode-xid-0.0.2

Name:           rust-unicode-xid-0.0.2
Version:        0.0.2
Release:        %autorelease
Summary:        Rust crate "unicode-xid"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-xid
#!RemoteAsset:  sha256:f69506a2561962651710609304bbb961fa3da598c812f877975a82e48ee144f9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/no-std) = %{version}

%description
Source code for takopackized Rust crate "unicode-xid"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
