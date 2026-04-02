# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name typenum
%global full_version 1.19.0
%global pkgname typenum-1.0

Name:           rust-typenum-1.0
Version:        1.19.0
Release:        %autorelease
Summary:        Rust crate "typenum"
License:        MIT OR Apache-2.0
URL:            https://github.com/paholg/typenum
#!RemoteAsset:  sha256:562d481066bde0658276a35467c4af00bdc6ee726305698a55b86e61d7ad82bb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-generics)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/force-unix-path-separator)
Provides:       crate(%{pkgname}/i128)
Provides:       crate(%{pkgname}/no-std)
Provides:       crate(%{pkgname}/strict)

%description
It currently supports bits, unsigned integers, and signed     integers. It also provides a type-level array of type-level numbers, but its     implementation is incomplete.
Source code for takopackized Rust crate "typenum"

%package     -n %{name}+scale-info
Summary:        Type-level numbers evaluated at     compile time - feature "scale_info"
Requires:       crate(%{pkgname})
Requires:       crate(scale-info-1.0) >= 1.0.0
Requires:       crate(scale-info-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/scale-info)

%description -n %{name}+scale-info
It currently supports bits, unsigned integers, and signed     integers. It also provides a type-level array of type-level numbers, but its     implementation is incomplete.
This metapackage enables feature "scale_info" for the Rust typenum crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
