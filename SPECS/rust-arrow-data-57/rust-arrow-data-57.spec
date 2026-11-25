# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-data
%global full_version 57.3.1
%global pkgname arrow-data-57

Name:           rust-arrow-data-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow-data"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:c1683705c63dcf0d18972759eda48489028cbbff67af7d6bef2c6b7b74ab778a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-buffer-57/default) >= 57.3.1
Requires:       crate(arrow-schema-57/default) >= 57.3.1
Requires:       crate(half-2) >= 2.1.0
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/std) >= 0.2.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/force-validate) = %{version}

%description
Source code for takopackized Rust crate "arrow-data"

%package     -n %{name}+ffi
Summary:        Array data abstractions for Apache Arrow - feature "ffi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrow-schema-57/ffi) >= 57.3.1
Provides:       crate(%{pkgname}/ffi) = %{version}

%description -n %{name}+ffi
This metapackage enables feature "ffi" for the Rust arrow-data crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
