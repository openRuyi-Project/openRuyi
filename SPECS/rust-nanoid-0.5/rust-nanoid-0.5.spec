# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name nanoid
%global full_version 0.5.0
%global pkgname nanoid-0.5

Name:           rust-nanoid-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "nanoid"
License:        MIT
URL:            https://github.com/mrdimidium/nanoid
#!RemoteAsset:  sha256:8628de41fe064cc3f0cf07f3d299ee3e73521adaff72278731d5c8cae3797873
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "nanoid"

%package     -n %{name}+smartstring
Summary:        Tiny, secure, URL-friendly, unique string ID generator for Rust - feature "smartstring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smartstring-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/smartstring) = %{version}

%description -n %{name}+smartstring
This metapackage enables feature "smartstring" for the Rust nanoid crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
