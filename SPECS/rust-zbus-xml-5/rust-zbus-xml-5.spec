# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zbus_xml
%global full_version 5.1.1
%global pkgname zbus-xml-5

Name:           rust-zbus-xml-5
Version:        5.1.1
Release:        %autorelease
Summary:        Rust crate "zbus_xml"
License:        MIT
URL:            https://github.com/z-galaxy/zbus/
#!RemoteAsset:  sha256:a8067892e940ed1727dea64690378601603b31d62dfde019a5335fbb7c0e0ed9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quick-xml-0.39/default) >= 0.39.0
Requires:       crate(quick-xml-0.39/overlapped-lists) >= 0.39.0
Requires:       crate(quick-xml-0.39/serialize) >= 0.39.0
Requires:       crate(serde-1/default) >= 1.0.200
Requires:       crate(serde-1/derive) >= 1.0.200
Requires:       crate(zbus-names-4/default) >= 4.3.2
Requires:       crate(zvariant-5/default) >= 5.10.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zbus_xml"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
