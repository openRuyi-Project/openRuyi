# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name threadpool
%global full_version 1.8.1
%global pkgname threadpool-1.0

Name:           rust-threadpool-1.0
Version:        1.8.1
Release:        %autorelease
Summary:        Rust crate "threadpool"
License:        MIT/Apache-2.0
URL:            https://github.com/rust-threadpool/rust-threadpool
#!RemoteAsset:  sha256:d050e60b33d41c19108b32cea32164033a9013fe3b46cbd4457559bfbf77afaa
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-cpus-1.0/default) >= 1.13
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "threadpool"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
