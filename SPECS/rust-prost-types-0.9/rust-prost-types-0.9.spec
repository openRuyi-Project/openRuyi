# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-types
%global full_version 0.9.0
%global pkgname prost-types-0.9

Name:           rust-prost-types-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "prost-types"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:534b7a0e836e3c482d2693070f982e39e7611da9695d4d1f5a4b186b51faef0a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1) >= 1.0.0
Requires:       crate(prost-0.9/prost-derive) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "prost-types"

%package     -n %{name}+std
Summary:        Protocol Buffers implementation for the Rust Language - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-0.9/prost-derive) >= 0.9.0
Requires:       crate(prost-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust prost-types crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
