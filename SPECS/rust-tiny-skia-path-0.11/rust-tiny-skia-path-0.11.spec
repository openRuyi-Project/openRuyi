# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tiny-skia-path
%global full_version 0.11.4
%global pkgname tiny-skia-path-0.11

Name:           rust-tiny-skia-path-0.11
Version:        0.11.4
Release:        %autorelease
Summary:        Rust crate "tiny-skia-path"
License:        BSD-3-Clause
URL:            https://github.com/RazrFalcon/tiny-skia/tree/master/path
#!RemoteAsset:  sha256:9c9e7fc0c2e86a30b117d0462aa261b72b7a99b7ebd7deb3a14ceda95c5bdc93
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayref-0.3/default) >= 0.3.6
Requires:       crate(bytemuck-1/default) >= 1.4.0
Requires:       crate(strict-num-0.1) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "tiny-skia-path"

%package     -n %{name}+libm
Summary:        Tiny-skia Bezier path implementation - feature "libm" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libm-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/libm) = %{version}
Provides:       crate(%{pkgname}/no-std-float) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust tiny-skia-path crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "no-std-float" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
