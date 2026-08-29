# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zune-jpeg
%global full_version 0.5.15
%global pkgname zune-jpeg-0.5

Name:           rust-zune-jpeg-0.5
Version:        0.5.15
Release:        %autorelease
Summary:        Rust crate "zune-jpeg"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/etemesi254/zune-image/tree/dev/crates/zune-jpeg
#!RemoteAsset:  sha256:27bc9d5b815bc103f142aa054f561d9187d191692ec7c2d1e2b4737f8dbd7296
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zune-core-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/neon) = %{version}
Provides:       crate(%{pkgname}/portable-simd) = %{version}
Provides:       crate(%{pkgname}/x86) = %{version}

%description
Source code for takopackized Rust crate "zune-jpeg"

%package     -n %{name}+default
Summary:        Fast, correct and safe jpeg decoder - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/neon) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/x86) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zune-jpeg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Fast, correct and safe jpeg decoder - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zune-core-0.5/log) >= 0.5.1
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust zune-jpeg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast, correct and safe jpeg decoder - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zune-core-0.5/std) >= 0.5.1
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust zune-jpeg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
