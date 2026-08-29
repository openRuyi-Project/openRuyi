# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zeno
%global full_version 0.3.3
%global pkgname zeno-0.3

Name:           rust-zeno-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "zeno"
License:        Apache-2.0 OR MIT
URL:            https://github.com/dfrg/zeno
#!RemoteAsset:  sha256:6df3dc4292935e51816d896edcd52aa30bc297907c26167fec31e2b0c6a32524
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/eval) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "zeno"

%package     -n %{name}+default
Summary:        High performance, low level 2D path rasterization - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/eval) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust zeno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        High performance, low level 2D path rasterization - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libm-0.2) >= 0.2.7
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust zeno crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
