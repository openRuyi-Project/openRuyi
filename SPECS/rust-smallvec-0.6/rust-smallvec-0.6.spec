# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smallvec
%global full_version 0.6.14
%global pkgname smallvec-0.6

Name:           rust-smallvec-0.6
Version:        0.6.14
Release:        %autorelease
Summary:        Rust crate "smallvec"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-smallvec
#!RemoteAsset:  sha256:b97fcaeba89edba30f044a10c6a3cc39df9c3f17d7cd829dd1446cab35f890e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(maybe-uninit-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/may-dangle) = %{version}
Provides:       crate(%{pkgname}/specialization) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/union) = %{version}

%description
Source code for takopackized Rust crate "smallvec"

%package     -n %{name}+serde
Summary:        'Small vector' optimization: store up to a small number of items on the stack - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust smallvec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
