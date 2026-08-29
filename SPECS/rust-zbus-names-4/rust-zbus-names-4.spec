# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zbus_names
%global full_version 4.3.2
%global pkgname zbus-names-4

Name:           rust-zbus-names-4
Version:        4.3.2
Release:        %autorelease
Summary:        Rust crate "zbus_names"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:7074f3e50b894eac91750142016d30d0a89be8e67dbfd9704fb875825760e52d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(serde-1/default) >= 1.0.200
Requires:       crate(serde-1/derive) >= 1.0.200
Requires:       crate(winnow-1/default) >= 1.0.0
Requires:       crate(zvariant-5/default) >= 5.10.1
Requires:       crate(zvariant-5/enumflags2) >= 5.10.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zbus_names"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
