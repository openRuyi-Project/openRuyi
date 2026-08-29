# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-types
%global full_version 0.12.6
%global pkgname prost-types-0.12

Name:           rust-prost-types-0.12
Version:        0.12.6
Release:        %autorelease
Summary:        Rust crate "prost-types"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:9091c90b0a32608e984ff2fa4091273cbdd755d54935c51d520887f4a1dbd5b0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(prost-0.12/prost-derive) >= 0.12.6
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "prost-types"

%package     -n %{name}+std
Summary:        Prost definitions of Protocol Buffers well known types - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-0.12/prost-derive) >= 0.12.6
Requires:       crate(prost-0.12/std) >= 0.12.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust prost-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
