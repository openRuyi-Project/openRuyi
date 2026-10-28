# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vm-allocator
%global full_version 0.1.4
%global pkgname vm-allocator-0.1

Name:           rust-vm-allocator-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "vm-allocator"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vm-allocator
#!RemoteAsset:  sha256:a2feb549d049009150155ab6e1b0c8c0db9ea6805ba5bdc57a27a3b7466e80f5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(thiserror-2) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "vm-allocator"

%package     -n %{name}+serde
Summary:        Helpers for allocating resources needed during the lifetime of a VM - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.137
Requires:       crate(serde-1/derive) >= 1.0.137
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust vm-allocator crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
