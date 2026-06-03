# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name referencing
%global full_version 0.29.1
%global pkgname referencing-0.29

Name:           rust-referencing-0.29
Version:        0.29.1
Release:        %autorelease
Summary:        Rust crate "referencing"
License:        MIT
URL:            https://github.com/Stranger6667/jsonschema
#!RemoteAsset:  sha256:40a64b3a635fad9000648b4d8a59c8710c523ab61a23d392a7d91d47683f5adc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.12
Requires:       crate(ahash-0.8/serde) >= 0.8.12
Requires:       crate(fluent-uri-0.3/default) >= 0.3.2
Requires:       crate(fluent-uri-0.3/serde) >= 0.3.2
Requires:       crate(once-cell-1.0/default) >= 1.21.3
Requires:       crate(parking-lot-0.12/default) >= 0.12.4
Requires:       crate(percent-encoding-2.0/default) >= 2.3.1
Requires:       crate(serde-json-1.0/default) >= 1.0.140
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "referencing"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
