# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name servo_arc
%global full_version 0.4.3
%global pkgname servo-arc-0.4

Name:           rust-servo-arc-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "servo_arc"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/stylo
#!RemoteAsset:  sha256:170fb83ab34de17dc69aa7c67482b22218ddb85da56546f9bd6b929e32a05930
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(stable-deref-trait-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gecko-refcount-logging) = %{version}
Provides:       crate(%{pkgname}/track-alloc-size) = %{version}

%description
Source code for takopackized Rust crate "servo_arc"

%package     -n %{name}+serde
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust servo_arc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+servo
Summary:        Fork of std::sync::Arc with some extra functionality and without weak references - feature "servo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/track-alloc-size) = %{version}
Provides:       crate(%{pkgname}/servo) = %{version}

%description -n %{name}+servo
This metapackage enables feature "servo" for the Rust servo_arc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
