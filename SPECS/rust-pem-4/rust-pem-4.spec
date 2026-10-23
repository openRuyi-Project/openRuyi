# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pem
%global full_version 4.0.0
%global pkgname pem-4

Name:           rust-pem-4
Version:        4.0.0
Release:        %autorelease
Summary:        Rust crate "pem"
License:        MIT
URL:            https://github.com/jcreekmore/pem-rs.git
#!RemoteAsset:  sha256:d354a98a3d1251555de99e8fdd8afda05573c31b82f59063a7b0a29b5527f120
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.23/alloc) >= 0.23.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pem"

%package     -n %{name}+serde
Summary:        Parse and encode PEM-encoded data - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pem crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Parse and encode PEM-encoded data - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.23/alloc) >= 0.23.0
Requires:       crate(base64-0.23/std) >= 0.23.0
Requires:       crate(serde-core-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pem crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
