# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vfio_user
%global full_version 0.1.3
%global pkgname vfio-user-0.1

Name:           rust-vfio-user-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "vfio_user"
License:        Apache-2.0
URL:            https://github.com/rust-vmm/vfio-user
#!RemoteAsset:  sha256:731c2582dd43f4f174ab47b4c933a1a9bb872d9d1b7f54c5867e12dbc1491b75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.9.4
Requires:       crate(libc-0.2/default) >= 0.2.139
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(serde-1/default) >= 1.0.151
Requires:       crate(serde-1/rc) >= 1.0.151
Requires:       crate(serde-derive-1/default) >= 1.0.149
Requires:       crate(serde-json-1/default) >= 1.0.93
Requires:       crate(thiserror-2/default) >= 2.0.16
Requires:       crate(vfio-bindings-0.6/default) >= 0.6.2
Requires:       crate(vfio-bindings-0.6/fam-wrappers) >= 0.6.2
Requires:       crate(vm-memory-0.16/backend-atomic) >= 0.16.0
Requires:       crate(vm-memory-0.16/backend-mmap) >= 0.16.0
Requires:       crate(vm-memory-0.16/default) >= 0.16.0
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "vfio_user"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
