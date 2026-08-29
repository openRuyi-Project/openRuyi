# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num_threads
%global full_version 0.1.7
%global pkgname num-threads-0.1

Name:           rust-num-threads-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "num_threads"
License:        MIT OR Apache-2.0
URL:            https://github.com/jhpratt/num_threads
#!RemoteAsset:  sha256:5c7398b9c8b70908f6371f47ed36737907c87c52af34c268fed0bf0ceb92ead9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.107
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "num_threads"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
