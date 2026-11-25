# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ipnetwork
%global full_version 0.21.1
%global pkgname ipnetwork-0.21

Name:           rust-ipnetwork-0.21
Version:        0.21.1
Release:        %autorelease
Summary:        Rust crate "ipnetwork"
License:        MIT OR Apache-2.0
URL:            https://github.com/achanda/ipnetwork
#!RemoteAsset:  sha256:cf370abdafd54d13e54a620e8c3e1145f28e46cc9d704bc6d94414559df41763
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ipnetwork"

%package     -n %{name}+schemars
Summary:        Work with IP CIDRs in Rust - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-0.8/default) >= 0.8.17
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust ipnetwork crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Work with IP CIDRs in Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.200
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ipnetwork crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
