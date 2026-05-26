# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atomic
%global full_version 0.6.1
%global pkgname atomic-0.6

Name:           rust-atomic-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "atomic"
License:        Apache-2.0/MIT
URL:            https://github.com/Amanieu/atomic-rs
#!RemoteAsset:  sha256:a89cbf775b137e9b968e67227ef7f775587cde3fd31b0d8599dbd0f598a48340
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1.0/default) >= 1.25.0
Provides:       crate(atomic) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fallback)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "atomic"

%package     -n %{name}+serde
Summary:        Generic Atomic<T> wrapper type - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.219
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust atomic crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
