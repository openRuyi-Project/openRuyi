# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fastrand
%global full_version 2.4.1
%global pkgname fastrand-2

Name:           rust-fastrand-2
Version:        2.4.1
Release:        %autorelease
Summary:        Rust crate "fastrand"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/fastrand
#!RemoteAsset:  sha256:9f1f227452a390804cdb637b74a86990f2a7d7ba4b7d5693aac9b4dd6defd8d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "fastrand"

%package     -n %{name}+getrandom
Summary:        Simple and fast random number generator - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(getrandom-0.3/default) >= 0.3.4
Requires:       crate(getrandom-0.3/wasm-js) >= 0.3.4
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust fastrand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js
Summary:        Simple and fast random number generator - feature "js"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/js) = %{version}

%description -n %{name}+js
This metapackage enables feature "js" for the Rust fastrand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
