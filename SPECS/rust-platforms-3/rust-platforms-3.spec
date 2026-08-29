# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name platforms
%global full_version 3.12.0
%global pkgname platforms-3

Name:           rust-platforms-3
Version:        3.12.0
Release:        %autorelease
Summary:        Rust crate "platforms"
License:        Apache-2.0 OR MIT
URL:            https://rustsec.org
#!RemoteAsset:  sha256:9245c6e7c5a6bcdd7977fdf6d1e1c67f4cc2d0d58c041df0ea5940953033e6ca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "platforms"

%package     -n %{name}+serde
Summary:        Rust platform registry with information about valid Rust platforms (target triple, target_arch, target_os) sourced from the Rust compiler - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust platforms crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
