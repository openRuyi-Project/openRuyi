# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kvm-ioctls
%global full_version 0.24.0
%global pkgname kvm-ioctls-0.24

Name:           rust-kvm-ioctls-0.24
Version:        0.24.0
Release:        %autorelease
Summary:        Rust crate "kvm-ioctls"
License:        Apache-2.0 OR MIT
URL:            https://github.com/rust-vmm/kvm
#!RemoteAsset:  sha256:333f77a20344a448f3f70664918135fddeb804e938f28a99d685bd92926e0b19
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.1
Requires:       crate(kvm-bindings-0.14/default) >= 0.14.0
Requires:       crate(kvm-bindings-0.14/fam-wrappers) >= 0.14.0
Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(vmm-sys-util-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "kvm-ioctls"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
