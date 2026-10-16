# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gethostname
%global full_version 0.4.3
%global pkgname gethostname-0.4

Name:           rust-gethostname-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "gethostname"
License:        Apache-2.0
URL:            https://github.com/swsnr/gethostname.rs
#!RemoteAsset:  sha256:0176e0459c2e4a1fe232f984bca6890e681076abb9934f6cea7c326f3fc47818
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.141
Requires:       crate(windows-targets-0.48/default) >= 0.48.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gethostname"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
