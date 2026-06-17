# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aligned-vec
%global full_version 0.6.4
%global pkgname aligned-vec-0.6

Name:           rust-aligned-vec-0.6
Version:        0.6.4
Release:        %autorelease
Summary:        Rust crate "aligned-vec"
License:        MIT
URL:            https://github.com/sarah-ek/aligned-vec/
#!RemoteAsset:  sha256:dc890384c8602f339876ded803c97ad529f3842aba97f6392b3dba0dd171769b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(equator-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "aligned-vec"

%package     -n %{name}+serde
Summary:        Aligned vector and box containers - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust aligned-vec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
