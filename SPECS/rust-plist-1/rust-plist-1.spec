# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plist
%global full_version 1.10.1
%global pkgname plist-1

Name:           rust-plist-1
Version:        1.10.1
Release:        %autorelease
Summary:        Rust crate "plist"
License:        MIT
URL:            https://github.com/ebarnard/rust-plist/
#!RemoteAsset:  sha256:2896bade328c13f7042a297ea5ac5b0951f6cf989dea5f32c2fd98da398195cb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.23/default) >= 0.23.1
Requires:       crate(indexmap-2/default) >= 2.14.0
Requires:       crate(quick-xml-0.42/default) >= 0.42.0
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/enable-unstable-features-that-may-break-with-minor-version-bumps) = %{version}

%description
Supports Serde serialization.
Source code for takopackized Rust crate "plist"

%package     -n %{name}+serde
Summary:        Rusty plist parser - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Supports Serde serialization.
This metapackage enables feature "serde" for the Rust plist crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
