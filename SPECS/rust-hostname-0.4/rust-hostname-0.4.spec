# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hostname
%global full_version 0.4.1
%global pkgname hostname-0.4

Name:           rust-hostname-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "hostname"
License:        MIT
URL:            https://github.com/svartalf/hostname
#!RemoteAsset:  sha256:a56f203cd1c76362b69e3863fd987520ac36cf70a8c92627449b2f64a8cf7d65
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(windows-link-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/set) = %{version}

%description
Source code for takopackized Rust crate "hostname"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
