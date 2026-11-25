# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sea-schema-derive
%global full_version 0.3.0
%global pkgname sea-schema-derive-0.3

Name:           rust-sea-schema-derive-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "sea-schema-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/SeaQL/sea-schema
#!RemoteAsset:  sha256:debdc8729c37fdbf88472f97fd470393089f997a909e535ff67c544d18cfccf0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4) >= 0.4.0
Requires:       crate(proc-macro2-1) >= 1.0.0
Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-2/derive) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(syn-2/printing) >= 2.0.0
Requires:       crate(syn-2/proc-macro) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sea-schema-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
