# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dir-lock
%global full_version 0.5.0
%global pkgname dir-lock-0.5

Name:           rust-dir-lock-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "dir-lock"
License:        MIT
URL:            https://github.com/fenhl/rust-dir-lock
#!RemoteAsset:  sha256:df6e616b67e0e0057a0952ef9991d66300044b897b879ef6fa89851495065b35
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sysinfo-0.35/system) >= 0.35.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dir-lock"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
