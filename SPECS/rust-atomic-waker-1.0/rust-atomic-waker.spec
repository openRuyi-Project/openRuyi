# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name atomic-waker
%global full_version 1.1.2
%global pkgname atomic-waker-1.0

Name:           rust-atomic-waker-1.0
Version:        1.1.2
Release:        %autorelease
Summary:        Rust crate "atomic-waker"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/atomic-waker
#!RemoteAsset:  sha256:1505bd5d3d116872e7271a6d4e16d81d0c8570876c8de68093a09ac269d8aac0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "atomic-waker"

%package     -n %{name}+portable-atomic
Summary:        Synchronization primitive for task wakeup - feature "portable-atomic"
Requires:       crate(%{pkgname})
Requires:       crate(portable-atomic-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust atomic-waker crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
