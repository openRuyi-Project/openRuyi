# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name string_cache_codegen
%global full_version 0.4.4
%global pkgname string-cache-codegen-0.4

Name:           rust-string-cache-codegen-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "string_cache_codegen"
License:        MIT  OR  Apache-2.0
URL:            https://github.com/servo/string-cache
#!RemoteAsset:  sha256:f0f45ed1b65bf9a4bf2f7b7dc59212d1926e9eaf00fa998988e420fd124467c6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-generator-0.7/default) >= 0.7.15
Requires:       crate(phf-shared-0.7/default) >= 0.7.4
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(string-cache-shared-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "string_cache_codegen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
