# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name multimap
%global full_version 0.8.3
%global pkgname multimap-0.8

Name:           rust-multimap-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "multimap"
License:        MIT OR Apache-2.0
URL:            https://github.com/havarnov/multimap
#!RemoteAsset:  sha256:e5ce46fe64a9d73be07dcbe690a38ce1b293be448fd8ce1e6c1b8062c9f72c6a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "multimap"

%package     -n %{name}+serde
Summary:        Multimap implementation - feature "serde" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde-impl) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust multimap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "serde_impl" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
