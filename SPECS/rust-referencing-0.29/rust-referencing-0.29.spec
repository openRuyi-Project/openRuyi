# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name referencing
%global full_version 0.29.0
%global pkgname referencing-0.29

Name:           rust-referencing-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "referencing"
License:        MIT
URL:            https://github.com/Stranger6667/jsonschema
#!RemoteAsset:  sha256:6ce52678d53e5ee37e4af0a9036ca834d0cd34b33c82457c6b06a24f8d783344
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.0
Requires:       crate(ahash-0.8/serde) >= 0.8.0
Requires:       crate(fluent-uri-0.3/default) >= 0.3.2
Requires:       crate(fluent-uri-0.3/serde) >= 0.3.2
Requires:       crate(once-cell-1/default) >= 1.20.1
Requires:       crate(parking-lot-0.12/default) >= 0.12.3
Requires:       crate(percent-encoding-2/default) >= 2.3.1
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "referencing"

%package     -n %{name}+retrieve-async
Summary:        Implementation-agnostic JSON reference resolution library for Rust - feature "retrieve-async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.86
Requires:       crate(futures-0.3/default) >= 0.3.31
Provides:       crate(%{pkgname}/retrieve-async) = %{version}

%description -n %{name}+retrieve-async
This metapackage enables feature "retrieve-async" for the Rust referencing crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
