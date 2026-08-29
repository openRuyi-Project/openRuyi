# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vfio-bindings
%global full_version 0.6.2
%global pkgname vfio-bindings-0.6

Name:           rust-vfio-bindings-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "vfio-bindings"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vfio
#!RemoteAsset:  sha256:188dac3057a0cbc94470085204c84b82ff7ec5dac629a514323cd133d1f9abe0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/vfio-v5-0-0) = %{version}

%description
Source code for takopackized Rust crate "vfio-bindings"

%package     -n %{name}+vmm-sys-util
Summary:        Rust FFI bindings to vfio generated using bindgen - feature "vmm-sys-util" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/fam-wrappers) = %{version}
Provides:       crate(%{pkgname}/vmm-sys-util) = %{version}

%description -n %{name}+vmm-sys-util
This metapackage enables feature "vmm-sys-util" for the Rust vfio-bindings crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fam-wrappers" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
