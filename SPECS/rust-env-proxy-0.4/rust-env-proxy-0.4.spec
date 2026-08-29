# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name env_proxy
%global full_version 0.4.1
%global pkgname env-proxy-0.4

Name:           rust-env-proxy-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "env_proxy"
License:        MIT OR Apache-2.0
URL:            https://github.com/inejge/env_proxy
#!RemoteAsset:  sha256:3a5019be18538406a43b5419a5501461f0c8b49ea7dfda0cfc32f4e51fc44be1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(url-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "env_proxy"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
