# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper-timeout
%global full_version 0.4.1
%global pkgname hyper-timeout-0.4

Name:           rust-hyper-timeout-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "hyper-timeout"
License:        MIT OR Apache-2.0
URL:            https://github.com/hjr3/hyper-timeout
#!RemoteAsset:  sha256:bbb958482e8c7be4bc3cf272a766a2b0bf1a6755e7a6ae777f017a31d11b13b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hyper-0.14/client) >= 0.14.2
Requires:       crate(hyper-0.14/default) >= 0.14.2
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-io-timeout-1/default) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hyper-timeout"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
