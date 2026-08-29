# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ipnetwork
%global full_version 0.20.0
%global pkgname ipnetwork-0.20

Name:           rust-ipnetwork-0.20
Version:        0.20.0
Release:        %autorelease
Summary:        Rust crate "ipnetwork"
License:        MIT OR Apache-2.0
URL:            https://github.com/achanda/ipnetwork
#!RemoteAsset:  sha256:bf466541e9d546596ee94f9f69590f89473455f88372423e0008fc1a7daf100e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ipnetwork"

%package     -n %{name}+schemars
Summary:        Work with IP CIDRs in Rust - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-0.8/default) >= 0.8.10
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust ipnetwork crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Work with IP CIDRs in Rust - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ipnetwork crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
