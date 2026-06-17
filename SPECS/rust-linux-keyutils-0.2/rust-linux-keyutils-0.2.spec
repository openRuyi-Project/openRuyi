# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linux-keyutils
%global full_version 0.2.5
%global pkgname linux-keyutils-0.2

Name:           rust-linux-keyutils-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "linux-keyutils"
License:        Apache-2.0 OR MIT
URL:            https://github.com/landhb/linux-keyutils
#!RemoteAsset:  sha256:83270a18e9f90d0707c41e9f35efada77b64c0e6f3f1810e71c8368a864d5590
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2) >= 2.6.0
Requires:       crate(libc-0.2) >= 0.2.158
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Provides a safe interface around the raw system calls allowing user-space programs to perform key manipulation.
Source code for takopackized Rust crate "linux-keyutils"

%package     -n %{name}+std
Summary:        Rust interface to the Linux key-management facility - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.6.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
Provides a safe interface around the raw system calls allowing user-space programs to perform key manipulation.
This metapackage enables feature "std" for the Rust linux-keyutils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
