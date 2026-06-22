# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pixman
%global full_version 0.2.1
%global pkgname pixman-0.2

Name:           rust-pixman-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "pixman"
License:        MIT
URL:            https://github.com/cmeissl/pixman-rs
#!RemoteAsset:  sha256:cea217d496c19ac0a8e502b37078e1f683d16344adee9eb247a5d57c165e1edf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(paste-1/default) >= 1.0.14
Requires:       crate(pixman-sys-0.1/default) >= 0.1.0
Requires:       crate(thiserror-1/default) >= 1.0.50
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}

%description
Source code for takopackized Rust crate "pixman"

%package     -n %{name}+drm-fourcc
Summary:        Low-level software library for pixel manipulation, providing features such as image compositing and trapezoid rasterization - feature "drm-fourcc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(drm-fourcc-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/drm-fourcc) = %{version}

%description -n %{name}+drm-fourcc
This metapackage enables feature "drm-fourcc" for the Rust pixman crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
