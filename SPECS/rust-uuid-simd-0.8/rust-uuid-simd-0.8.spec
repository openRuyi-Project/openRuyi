# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
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

Requires:       crate(outref-0.5/default) >= 0.5.0
Requires:       crate(vsimd-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "uuid-simd"

%package     -n %{name}+alloc
Summary:        SIMD-accelerated UUID operations - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vsimd-0.8/alloc) >= 0.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        SIMD-accelerated UUID operations - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/detect) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/uuid) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+detect
Summary:        SIMD-accelerated UUID operations - feature "detect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vsimd-0.8/detect) >= 0.8.0
Provides:       crate(%{pkgname}/detect) = %{version}

%description -n %{name}+detect
This metapackage enables feature "detect" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        SIMD-accelerated UUID operations - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(vsimd-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        SIMD-accelerated UUID operations - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vsimd-0.8/unstable) >= 0.8.0
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        SIMD-accelerated UUID operations - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.2.2
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust uuid-simd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
