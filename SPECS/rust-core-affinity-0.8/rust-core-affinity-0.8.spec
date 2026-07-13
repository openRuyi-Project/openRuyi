# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core_affinity
%global full_version 0.8.3
%global pkgname core-affinity-0.8

Name:           rust-core-affinity-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "core_affinity"
License:        MIT OR Apache-2.0
URL:            https://github.com/Elzair/core_affinity_rs
#!RemoteAsset:  sha256:a034b3a7b624016c6e13f5df875747cc25f884156aad2abd12b6c46797971342
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.30
Requires:       crate(num-cpus-1/default) >= 1.14.0
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.9
Requires:       crate(winapi-0.3/winbase) >= 0.3.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "core_affinity"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
