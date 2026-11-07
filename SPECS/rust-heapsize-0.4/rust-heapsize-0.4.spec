# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heapsize
%global full_version 0.4.2
%global pkgname heapsize-0.4

Name:           rust-heapsize-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "heapsize"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/heapsize
#!RemoteAsset:  sha256:1679e6ea370dee694f91f1dc469bf94cf8f52051d147aec3e1f9497c6fc22461
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.3/default) >= 0.3.4
Requires:       crate(winapi-0.3/heapapi) >= 0.3.4
Requires:       crate(winapi-0.3/std) >= 0.3.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/flexible-tests) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "heapsize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
