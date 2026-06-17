# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vm-memory
%global full_version 0.16.0
%global pkgname vm-memory-0.16

Name:           rust-vm-memory-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "vm-memory"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vm-memory
#!RemoteAsset:  sha256:e2919f87420b6998a131eb7c78843890295e91a3f8f786ccc925c8d387b75121
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(thiserror-1/default) >= 1.0.40
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/errhandlingapi) >= 0.3.0
Requires:       crate(winapi-0.3/sysinfoapi) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/backend-bitmap) = %{version}
Provides:       crate(%{pkgname}/backend-mmap) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vm-memory"

%package     -n %{name}+arc-swap
Summary:        Safe abstractions for accessing the VM physical memory - feature "arc-swap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arc-swap-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arc-swap) = %{version}
Provides:       crate(%{pkgname}/backend-atomic) = %{version}

%description -n %{name}+arc-swap
This metapackage enables feature "arc-swap" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "backend-atomic" feature.

%package     -n %{name}+bitflags
Summary:        Safe abstractions for accessing the VM physical memory - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vmm-sys-util
Summary:        Safe abstractions for accessing the VM physical memory - feature "vmm-sys-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vmm-sys-util-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname}/vmm-sys-util) = %{version}

%description -n %{name}+vmm-sys-util
This metapackage enables feature "vmm-sys-util" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xen
Summary:        Safe abstractions for accessing the VM physical memory - feature "xen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/backend-mmap) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/vmm-sys-util) = %{version}
Provides:       crate(%{pkgname}/xen) = %{version}

%description -n %{name}+xen
This metapackage enables feature "xen" for the Rust vm-memory crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
