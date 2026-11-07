# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heck
%global full_version 0.3.3
%global pkgname heck-0.3

Name:           rust-heck-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "heck"
License:        MIT OR Apache-2.0
URL:            https://github.com/withoutboats/heck
#!RemoteAsset:  sha256:6d621efb26863f0e9924c6ac577e8275e5e6b77455db64ffa6c65c904e9e132c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-segmentation-1/default) >= 1.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "heck"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
