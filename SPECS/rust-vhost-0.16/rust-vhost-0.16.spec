# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vhost
%global full_version 0.16.0
%global pkgname vhost-0.16

Name:           rust-vhost-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "vhost"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vhost
#!RemoteAsset:  sha256:ee90657203a8644e9a0860a0db6a7887d8ef0c7bc09fc22dfa4ae75df65bac86
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(uuid-1/default) >= 1.11.0
Requires:       crate(uuid-1/fast-rng) >= 1.11.0
Requires:       crate(uuid-1/v4) >= 1.11.0
Requires:       crate(vm-memory-0.17/backend-mmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/default) >= 0.17.1
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/postcopy) = %{version}
Provides:       crate(%{pkgname}/test-utils) = %{version}
Provides:       crate(%{pkgname}/vhost-kern) = %{version}
Provides:       crate(%{pkgname}/vhost-net) = %{version}
Provides:       crate(%{pkgname}/vhost-user) = %{version}
Provides:       crate(%{pkgname}/vhost-user-backend) = %{version}
Provides:       crate(%{pkgname}/vhost-user-frontend) = %{version}
Provides:       crate(%{pkgname}/vhost-vdpa) = %{version}
Provides:       crate(%{pkgname}/vhost-vsock) = %{version}

%description
Source code for takopackized Rust crate "vhost"

%package     -n %{name}+xen
Summary:        Pure rust library for vdpa, vhost and vhost-user - feature "xen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vm-memory-0.17/backend-mmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/xen) >= 0.17.1
Provides:       crate(%{pkgname}/xen) = %{version}

%description -n %{name}+xen
This metapackage enables feature "xen" for the Rust vhost crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
