# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wait-timeout
%global full_version 0.2.1
%global pkgname wait-timeout-0.2

Name:           rust-wait-timeout-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "wait-timeout"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/wait-timeout
#!RemoteAsset:  sha256:09ac3b126d3914f9849036f826e054cbabdc8519970b8998ddaf3b5bd3c65f11
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.56
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "wait-timeout"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
