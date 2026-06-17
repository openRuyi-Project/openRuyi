# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zune-core
%global full_version 0.5.1
%global pkgname zune-core-0.5

Name:           rust-zune-core-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "zune-core"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/etemesi254/zune-image
#!RemoteAsset:  sha256:cb8a0807f7c01457d0379ba880ba6322660448ddebc890ce29bb64da71fb40f9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "zune-core"

%package     -n %{name}+log
Summary:        Core utilities for image processing in the zune family of crates - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust zune-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Core utilities for image processing in the zune family of crates - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust zune-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
