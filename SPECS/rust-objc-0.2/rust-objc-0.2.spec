# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc
%global full_version 0.2.7
%global pkgname objc-0.2

Name:           rust-objc-0.2
Version:        0.2.7
Release:        %autorelease
Summary:        Rust crate "objc"
License:        MIT
URL:            http://github.com/SSheldon/rust-objc
#!RemoteAsset:  sha256:915b1b472bc21c53464d6c8461c9d3af805ba1ef837e1cac254428f4a77177b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-range-dependencies.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(malloc-buf-0.0.6/default) >= 0.0.6
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/verify-message) = %{version}

%description
Source code for takopackized Rust crate "objc"

%package     -n %{name}+objc-exception
Summary:        Objective-C Runtime bindings and wrapper for Rust - feature "objc_exception" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc-exception-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/exception) = %{version}
Provides:       crate(%{pkgname}/objc-exception) = %{version}

%description -n %{name}+objc-exception
This metapackage enables feature "objc_exception" for the Rust objc crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "exception" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
