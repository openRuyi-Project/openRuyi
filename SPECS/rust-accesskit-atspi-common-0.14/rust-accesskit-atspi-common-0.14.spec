# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name accesskit_atspi_common
%global full_version 0.14.2
%global pkgname accesskit-atspi-common-0.14

Name:           rust-accesskit-atspi-common-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "accesskit_atspi_common"
License:        MIT OR Apache-2.0
URL:            https://github.com/AccessKit/accesskit
#!RemoteAsset:  sha256:890d241cf51fc784f0ac5ac34dfc847421f8d39da6c7c91a0fcc987db62a8267
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(accesskit-0.21/default) >= 0.21.1
Requires:       crate(accesskit-consumer-0.31/default) >= 0.31.0
Requires:       crate(atspi-common-0.9) >= 0.9.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(zvariant-5) >= 5.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/simplified-api) = %{version}

%description
Source code for takopackized Rust crate "accesskit_atspi_common"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
