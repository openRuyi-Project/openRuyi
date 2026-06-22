# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name async-object-pool
%global full_version 0.2.0
%global pkgname async-object-pool-0.2

Name:           rust-async-object-pool-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "async-object-pool"
License:        MIT
URL:            https://github.com/alexliesenfeld/async-object-pool
#!RemoteAsset:  sha256:e1ac0219111eb7bb7cb76d4cf2cb50c598e7ae549091d3616f9e95442c18486f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(async-lock-3/default) >= 3.0.0
Requires:       crate(event-listener-5/default) >= 5.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "async-object-pool"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
