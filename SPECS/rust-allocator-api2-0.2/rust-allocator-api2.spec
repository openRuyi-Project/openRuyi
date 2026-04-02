# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name allocator-api2
%global full_version 0.2.21
%global pkgname allocator-api2-0.2

Name:           rust-allocator-api2-0.2
Version:        0.2.21
Release:        %autorelease
Summary:        Rust crate "allocator-api2"
License:        MIT OR Apache-2.0
URL:            https://github.com/zakarumych/allocator-api2
#!RemoteAsset:  sha256:683d7910e743518b0e34f1186f92494becacb047c7b6bf616c96772180fef923
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fresh-rust)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "allocator-api2"

%package     -n %{name}+serde
Summary:        Mirror of Rust's allocator API - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust allocator-api2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
