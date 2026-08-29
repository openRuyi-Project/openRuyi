# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name headers
%global full_version 0.4.1
%global pkgname headers-0.4

Name:           rust-headers-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "headers"
License:        MIT
URL:            https://hyper.rs
#!RemoteAsset:  sha256:b3314d5adb5d94bcdf56771f2e50dbbc80bb4bdf88967526706205ac9eff24eb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(headers-core-0.3/default) >= 0.3.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(httpdate-1/default) >= 1.0.0
Requires:       crate(mime-0.3/default) >= 0.3.14
Requires:       crate(sha1-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "headers"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
