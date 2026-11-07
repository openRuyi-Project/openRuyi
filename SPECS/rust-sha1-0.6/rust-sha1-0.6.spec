# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha1
%global full_version 0.6.1
%global pkgname sha1-0.6

Name:           rust-sha1-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "sha1"
License:        BSD-3-Clause
URL:            https://github.com/mitsuhiko/sha1-smol
#!RemoteAsset:  sha256:c1da05c97445caa12d05e848c4a4fcbbea29e748ac28f7e80e9b010392063770
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sha1-smol-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sha1"

%package     -n %{name}+serde
Summary:        Minimal dependency free implementation of SHA1 for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-smol-1/serde) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Minimal dependency free implementation of SHA1 for Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-smol-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
