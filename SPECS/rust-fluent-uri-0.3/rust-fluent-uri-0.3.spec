# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fluent-uri
%global full_version 0.3.2
%global pkgname fluent-uri-0.3

Name:           rust-fluent-uri-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "fluent-uri"
License:        MIT
URL:            https://github.com/yescallop/fluent-uri-rs
#!RemoteAsset:  sha256:1918b65d96df47d3591bed19c5cca17e3fa5d0707318e4b5ef2eae01764df7e5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(borrow-or-share-0.2/default) >= 0.2.0
Requires:       crate(ref-cast-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/net) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "fluent-uri"

%package     -n %{name}+serde
Summary:        Generic URI/IRI handling library compliant with RFC 3986/3987 - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust fluent-uri crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
