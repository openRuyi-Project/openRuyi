# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libudev-sys
%global full_version 0.1.4
%global pkgname libudev-sys-0.1

Name:           rust-libudev-sys-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "libudev-sys"
License:        MIT
URL:            https://github.com/dcuddeback/libudev-sys
#!RemoteAsset:  sha256:3c8469b4a23b962c1396b9b451dda50ef5b283e8dd309d69033475fa9b334324
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pkg-config-0.3) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "libudev-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
