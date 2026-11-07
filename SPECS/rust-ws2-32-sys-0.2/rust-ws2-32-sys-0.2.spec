# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ws2_32-sys
%global full_version 0.2.1
%global pkgname ws2-32-sys-0.2

Name:           rust-ws2-32-sys-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "ws2_32-sys"
License:        MIT
URL:            https://github.com/retep998/winapi-rs
#!RemoteAsset:  sha256:d59cefebd0c892fa2dd6de581e937301d8552cb44489cdff035c6187cb63fa5e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.2/default) >= 0.2.5
Requires:       crate(winapi-build-0.1) >= 0.1.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
See winapi for types and constants.
Source code for takopackized Rust crate "ws2_32-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
