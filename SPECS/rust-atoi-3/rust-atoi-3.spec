# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atoi
%global full_version 3.1.0
%global pkgname atoi-3

Name:           rust-atoi-3
Version:        3.1.0
Release:        %autorelease
Summary:        Rust crate "atoi"
License:        MIT
URL:            https://github.com/pacman82/atoi-rs
#!RemoteAsset:  sha256:e7a8bbe9949e43a1edaa043038c68703b04774156afdfb62ba2cef5bf93d67be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2) >= 0.2.14

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "atoi"

%package     -n %{name}+std
Summary:        Parse integers directly from `[u8]` slices in safe code - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/std) >= 0.2.14
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust atoi crate, by pulling
in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
