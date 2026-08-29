# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name accesskit_consumer
%global full_version 0.31.0
%global pkgname accesskit-consumer-0.31

Name:           rust-accesskit-consumer-0.31
Version:        0.31.0
Release:        %autorelease
Summary:        Rust crate "accesskit_consumer"
License:        MIT OR Apache-2.0
URL:            https://github.com/AccessKit/accesskit
#!RemoteAsset:  sha256:db81010a6895d8707f9072e6ce98070579b43b717193d2614014abd5cb17dd43
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(accesskit-0.21/default) >= 0.21.1
Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "accesskit_consumer"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
