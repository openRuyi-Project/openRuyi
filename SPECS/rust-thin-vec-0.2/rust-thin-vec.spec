# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name thin-vec
%global full_version 0.2.14
%global pkgname thin-vec-0.2

Name:           rust-thin-vec-0.2
Version:        0.2.14
Release:        %autorelease
Summary:        Rust crate "thin-vec"
License:        MIT/Apache-2.0
URL:            https://github.com/gankra/thin-vec
#!RemoteAsset:  sha256:144f754d318415ac792f9d69fc87abbbfc043ce2ef041c60f16ad828f638717d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/gecko-ffi)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "thin-vec"

%package     -n %{name}+malloc-size-of
Summary:        Vec that takes up less space on the stack - feature "malloc_size_of"
Requires:       crate(%{pkgname})
Requires:       crate(malloc-size-of-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/malloc-size-of)

%description -n %{name}+malloc-size-of
This metapackage enables feature "malloc_size_of" for the Rust thin-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Vec that takes up less space on the stack - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust thin-vec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
