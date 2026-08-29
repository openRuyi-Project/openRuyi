# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper-timeout
%global full_version 0.5.2
%global pkgname hyper-timeout-0.5

Name:           rust-hyper-timeout-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "hyper-timeout"
License:        MIT OR Apache-2.0
URL:            https://github.com/hjr3/hyper-timeout
#!RemoteAsset:  sha256:2b90d566bffbce6a75bd8b09a05aa8c2cb1fabb6cb348f8840c9e4c90a0d83b0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hyper-1/default) >= 1.1.0
Requires:       crate(hyper-util-0.1/client-legacy) >= 0.1.10
Requires:       crate(hyper-util-0.1/default) >= 0.1.10
Requires:       crate(hyper-util-0.1/http1) >= 0.1.10
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(tokio-1/default) >= 1.35.0
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hyper-timeout"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
