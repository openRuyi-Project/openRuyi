# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smol_str
%global full_version 0.2.2
%global pkgname smol-str-0.2

Name:           rust-smol-str-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "smol_str"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-analyzer/smol_str
#!RemoteAsset:  sha256:dd538fb6910ac1099850255cf94a94df6551fbdd602454387d0adb2d1ca6dead
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "smol_str"

%package     -n %{name}+arbitrary
Summary:        Small-string optimized string type with O(1) clone - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust smol_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Small-string optimized string type with O(1) clone - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.136
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust smol_str crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Small-string optimized string type with O(1) clone - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/std) >= 1.0.136
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust smol_str crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
