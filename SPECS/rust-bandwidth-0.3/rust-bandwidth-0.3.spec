# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bandwidth
%global full_version 0.3.0
%global pkgname bandwidth-0.3

Name:           rust-bandwidth-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "bandwidth"
License:        Apache-2.0
URL:            https://github.com/stack-rs/bandwidth
#!RemoteAsset:  sha256:7a464cd54c99441ba44d3d09f6f980f8c29d068645022852ab66cbaad42ef6a0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "bandwidth"

%package     -n %{name}+serde
Summary:        Representing bandwidth speed in a variety of units, mimicking the `core::time::Duration` struct - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.152
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bandwidth crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Representing bandwidth speed in a variety of units, mimicking the `core::time::Duration` struct - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.152
Requires:       crate(serde-1/std) >= 1.0.152
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bandwidth crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
