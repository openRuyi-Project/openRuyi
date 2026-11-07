# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iovec
%global full_version 0.1.4
%global pkgname iovec-0.1

Name:           rust-iovec-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "iovec"
License:        MIT OR Apache-2.0
URL:            https://github.com/carllerche/iovec
#!RemoteAsset:  sha256:b2b3ea6ff95e175473f8ffe6a7eb7c00d054240321b84c57051175fe3c1e075e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "iovec"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
