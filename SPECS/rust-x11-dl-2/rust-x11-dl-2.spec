# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name x11-dl
%global full_version 2.21.0
%global pkgname x11-dl-2

Name:           rust-x11-dl-2
Version:        2.21.0
Release:        %autorelease
Summary:        Rust crate "x11-dl"
License:        MIT
URL:            https://github.com/AltF02/x11-rs.git
#!RemoteAsset:  sha256:38735924fedd5314a6e548792904ed8c6de6636285cb9fec04d5b1db85c1516f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(once-cell-1/default) >= 1.17.0
Requires:       crate(pkg-config-0.3) >= 0.3.24
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "x11-dl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
