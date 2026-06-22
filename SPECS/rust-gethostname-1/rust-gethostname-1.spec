# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gethostname
%global full_version 1.1.0
%global pkgname gethostname-1

Name:           rust-gethostname-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "gethostname"
License:        Apache-2.0
URL:            https://codeberg.org/swsnr/gethostname.rs
#!RemoteAsset:  sha256:1bd49230192a3797a9a4d6abe9b3eed6f7fa4c8a8a4947977c6f80025f92cbd8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustix-1/system) >= 1.0.3
Requires:       crate(windows-link-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gethostname"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
