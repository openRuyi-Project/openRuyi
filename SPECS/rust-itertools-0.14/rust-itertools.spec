# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name itertools
%global full_version 0.14.0
%global pkgname itertools-0.14

Name:           rust-itertools-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "itertools"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-itertools/itertools
#!RemoteAsset:  sha256:2b192c782037fadd9cfa75548310488aabdbf3d2da73885b31bd0abd03351285
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1.0) >= 1.15.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/use-alloc)

%description
Source code for takopackized Rust crate "itertools"

%package     -n %{name}+use-std
Summary:        Extra iterator adaptors, iterator methods, free functions, and macros - feature "use_std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/use-alloc)
Requires:       crate(either-1.0/use-std) >= 1.15.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/use-std)

%description -n %{name}+use-std
This metapackage enables feature "use_std" for the Rust itertools crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
