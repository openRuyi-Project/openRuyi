# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name openssl-probe
%global full_version 0.1.6
%global pkgname openssl-probe-0.1

Name:           rust-openssl-probe-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "openssl-probe"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/openssl-probe
#!RemoteAsset:  sha256:d05e27ee213611ffe7d6348b942e8f942b37114c00cc03cec254295a4a17852e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "openssl-probe"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
