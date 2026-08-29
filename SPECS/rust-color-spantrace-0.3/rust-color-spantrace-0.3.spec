# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name color-spantrace
%global full_version 0.3.0
%global pkgname color-spantrace-0.3

Name:           rust-color-spantrace-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "color-spantrace"
License:        MIT OR Apache-2.0
URL:            https://github.com/eyre-rs/eyre
#!RemoteAsset:  sha256:b8b88ea9df13354b55bc7234ebcce36e6ef896aca2e42a15de9e10edce01b427
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(owo-colors-4/default) >= 4.0.0
Requires:       crate(tracing-core-0.1/default) >= 0.1.21
Requires:       crate(tracing-error-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "color-spantrace"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
