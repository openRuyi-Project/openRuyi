# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vm-fdt
%global full_version 0.3.0
%global pkgname vm-fdt-0.3

Name:           rust-vm-fdt-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "vm-fdt"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vm-fdt
#!RemoteAsset:  sha256:7e21282841a059bb62627ce8441c491f09603622cd5a21c43bfedc85a2952f23
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/long-running-test) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "vm-fdt"

%package     -n %{name}+hashbrown
Summary:        Writing Flattened Devicetree blobs - feature "hashbrown" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/hashbrown) = %{version}

%description -n %{name}+hashbrown
This metapackage enables feature "hashbrown" for the Rust vm-fdt crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "alloc" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
