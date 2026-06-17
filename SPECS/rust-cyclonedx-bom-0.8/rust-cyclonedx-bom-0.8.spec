# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cyclonedx-bom
%global full_version 0.8.1
%global pkgname cyclonedx-bom-0.8

Name:           rust-cyclonedx-bom-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "cyclonedx-bom"
License:        Apache-2.0
URL:            https://cyclonedx.org/
#!RemoteAsset:  sha256:3132b69ba8c13808bd2fa5748ac5b9816eb4f4e1f0bff6b7f9254a5940dcdeef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(cyclonedx-bom-macros-0.1/default) >= 0.1.0
Requires:       crate(fluent-uri-0.4/default) >= 0.4.1
Requires:       crate(indexmap-2/default) >= 2.2.2
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(ordered-float-5) >= 5.0.0
Requires:       crate(purl-0.1) >= 0.1.3
Requires:       crate(regex-1/default) >= 1.9.3
Requires:       crate(serde-1/default) >= 1.0.193
Requires:       crate(serde-1/derive) >= 1.0.193
Requires:       crate(serde-json-1/default) >= 1.0.108
Requires:       crate(spdx-0.13/default) >= 0.13.0
Requires:       crate(strum-0.28/default) >= 0.28.0
Requires:       crate(strum-0.28/derive) >= 0.28.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(time-0.3/default) >= 0.3.29
Requires:       crate(time-0.3/formatting) >= 0.3.29
Requires:       crate(time-0.3/parsing) >= 0.3.29
Requires:       crate(uuid-1/default) >= 1.6.1
Requires:       crate(uuid-1/v4) >= 1.6.1
Requires:       crate(xml-rs-0.8/default) >= 0.8.16
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cyclonedx-bom"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
