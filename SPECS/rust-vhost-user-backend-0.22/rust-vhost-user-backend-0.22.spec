# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vhost-user-backend
%global full_version 0.22.0
%global pkgname vhost-user-backend-0.22

Name:           rust-vhost-user-backend-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "vhost-user-backend"
License:        Apache-2.0
URL:            https://github.com/rust-vmm/vhost
#!RemoteAsset:  sha256:d5925983d8fb537752ad3e26604c0a17abfa5de77cb6773a096c8a959c9eca0f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(vhost-0.16/default) >= 0.16.0
Requires:       crate(vhost-0.16/vhost-user-backend) >= 0.16.0
Requires:       crate(virtio-bindings-0.2/default) >= 0.2.6
Requires:       crate(virtio-queue-0.17/default) >= 0.17.0
Requires:       crate(vm-memory-0.17/backend-atomic) >= 0.17.1
Requires:       crate(vm-memory-0.17/backend-bitmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/backend-mmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/default) >= 0.17.1
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vhost-user-backend"

%package     -n %{name}+postcopy
Summary:        Framework to build vhost-user backend service daemon - feature "postcopy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/userfaultfd) = %{version}
Requires:       crate(vhost-0.16/postcopy) >= 0.16.0
Requires:       crate(vhost-0.16/vhost-user-backend) >= 0.16.0
Provides:       crate(%{pkgname}/postcopy) = %{version}

%description -n %{name}+postcopy
This metapackage enables feature "postcopy" for the Rust vhost-user-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+userfaultfd
Summary:        Framework to build vhost-user backend service daemon - feature "userfaultfd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(userfaultfd-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/userfaultfd) = %{version}

%description -n %{name}+userfaultfd
This metapackage enables feature "userfaultfd" for the Rust vhost-user-backend crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+xen
Summary:        Framework to build vhost-user backend service daemon - feature "xen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vhost-0.16/vhost-user-backend) >= 0.16.0
Requires:       crate(vhost-0.16/xen) >= 0.16.0
Requires:       crate(vm-memory-0.17/backend-atomic) >= 0.17.1
Requires:       crate(vm-memory-0.17/backend-bitmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/backend-mmap) >= 0.17.1
Requires:       crate(vm-memory-0.17/xen) >= 0.17.1
Provides:       crate(%{pkgname}/xen) = %{version}

%description -n %{name}+xen
This metapackage enables feature "xen" for the Rust vhost-user-backend crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
