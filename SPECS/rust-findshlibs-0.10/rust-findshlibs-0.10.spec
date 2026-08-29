# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name findshlibs
%global full_version 0.10.2
%global pkgname findshlibs-0.10

Name:           rust-findshlibs-0.10
Version:        0.10.2
Release:        %autorelease
Summary:        Rust crate "findshlibs"
License:        MIT OR Apache-2.0
URL:            https://github.com/gimli-rs/findshlibs
#!RemoteAsset:  sha256:40b9e59cd0f7e0806cca4be089683ecb6434e602038df21fe6bf6711b2f07f64
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.67
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(libc-0.2/default) >= 0.2.104
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/libloaderapi) >= 0.3.9
Requires:       crate(winapi-0.3/memoryapi) >= 0.3.9
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.9
Requires:       crate(winapi-0.3/psapi) >= 0.3.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "findshlibs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
