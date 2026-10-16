# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name daemonize
%global full_version 0.5.0
%global pkgname daemonize-0.5

Name:           rust-daemonize-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "daemonize"
License:        MIT OR Apache-2.0
URL:            https://github.com/knsd/daemonize
#!RemoteAsset:  sha256:ab8bfdaacb3c887a54d41bdf48d3af8873b3f5566469f8ba21b92057509f116e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.98

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "daemonize"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
