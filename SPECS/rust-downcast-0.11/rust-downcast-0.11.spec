# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name downcast
%global full_version 0.11.0
%global pkgname downcast-0.11

Name:           rust-downcast-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "downcast"
License:        MIT
URL:            https://github.com/fkoep/downcast-rs
#!RemoteAsset:  sha256:1435fa1053d8b2fbbe9be7e97eca7f33d37b28409959813daefc1446a14247f1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "downcast"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
