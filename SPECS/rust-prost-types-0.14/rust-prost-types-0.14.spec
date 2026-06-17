# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-types
%global full_version 0.14.1
%global pkgname prost-types-0.14

Name:           rust-prost-types-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "prost-types"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:b9b4db3d6da204ed77bb26ba83b6122a73aeb2e87e25fbf7ad2e84c4ccbf8f72
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(prost-0.14/derive) >= 0.14.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "prost-types"

%package     -n %{name}+arbitrary
Summary:        Prost definitions of Protocol Buffers well known types - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.4.0
Requires:       crate(arbitrary-1/derive) >= 1.4.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust prost-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Prost definitions of Protocol Buffers well known types - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4) >= 0.4.34
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust prost-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Prost definitions of Protocol Buffers well known types - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-0.14/derive) >= 0.14.1
Requires:       crate(prost-0.14/std) >= 0.14.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust prost-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
