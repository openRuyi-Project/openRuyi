# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uuid-simd
%global full_version 0.8.0
%global pkgname uuid-simd-0.8

Name:           rust-uuid-simd-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "uuid-simd"
License:        MIT
URL:            https://github.com/Nugine/simd
#!RemoteAsset:  sha256:23b082222b4f6619906941c17eb2297fff4c2fb96cb60164170522942a200bd8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(outref-0.5/default) >= 0.5.2
Requires:       crate(vsimd-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "uuid-simd"

%package     -n %{name}+alloc
Summary:        SIMD-accelerated UUID operations - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(vsimd-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        SIMD-accelerated UUID operations - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/detect)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/uuid)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+detect
Summary:        SIMD-accelerated UUID operations - feature "detect"
Requires:       crate(%{pkgname})
Requires:       crate(vsimd-0.8/detect) >= 0.8.0
Provides:       crate(%{pkgname}/detect)

%description -n %{name}+detect
This metapackage enables feature "detect" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        SIMD-accelerated UUID operations - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(vsimd-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        SIMD-accelerated UUID operations - feature "unstable"
Requires:       crate(%{pkgname})
Requires:       crate(vsimd-0.8/unstable) >= 0.8.0
Provides:       crate(%{pkgname}/unstable)

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        SIMD-accelerated UUID operations - feature "uuid"
Requires:       crate(%{pkgname})
Requires:       crate(uuid-1.0/default) >= 1.17.0
Provides:       crate(%{pkgname}/uuid)

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
