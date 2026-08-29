# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pnet_base
%global full_version 0.35.0
%global pkgname pnet-base-0.35

Name:           rust-pnet-base-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "pnet_base"
License:        MIT OR Apache-2.0
URL:            https://github.com/libpnet/libpnet
#!RemoteAsset:  sha256:ffc190d4067df16af3aba49b3b74c469e611cad6314676eaf1157f31aa0fb2f7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(no-std-net-0.6) >= 0.6.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pnet_base"

%package     -n %{name}+serde
Summary:        Fundamental base types and code used by pnet - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.171
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pnet_base crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fundamental base types and code used by pnet - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(no-std-net-0.6/std) >= 0.6.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pnet_base crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
