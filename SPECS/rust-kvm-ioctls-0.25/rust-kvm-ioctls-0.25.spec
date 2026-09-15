# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kvm-ioctls
%global full_version 0.25.0
%global pkgname kvm-ioctls-0.25

Name:           rust-kvm-ioctls-0.25
Version:        0.25.0
Release:        %autorelease
Summary:        Rust crate "kvm-ioctls"
License:        Apache-2.0 OR MIT
URL:            https://github.com/rust-vmm/kvm
#!RemoteAsset:  sha256:06ac372c120eb893b086d1a12027669cf2b478d1f71204021ffa7adf57948d63
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

# Select an already packaged compatibility series within the upstream range.
Patch2000:      2000-use-packaged-vmm-sys-util.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.1
Requires:       crate(kvm-bindings-0.14/default) >= 0.14.1
Requires:       crate(kvm-bindings-0.14/fam-wrappers) >= 0.14.1
Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for the Rust crate "kvm-ioctls"

%files
%license LICENSE-APACHE LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
