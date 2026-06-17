# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kvm-bindings
%global full_version 0.14.0
%global pkgname kvm-bindings-0.14

Name:           rust-kvm-bindings-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "kvm-bindings"
License:        Apache-2.0
URL:            https://github.com/rust-vmm/kvm
#!RemoteAsset:  sha256:4b3c06ff73c7ce03e780887ec2389d62d2a2a9ddf471ab05c2ff69207cd3f3b4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "kvm-bindings"

%package     -n %{name}+serde
Summary:        Rust FFI bindings to KVM generated using bindgen - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(zerocopy-0.8/default) >= 0.8.23
Requires:       crate(zerocopy-0.8/derive) >= 0.8.23
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust kvm-bindings crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vmm-sys-util
Summary:        Rust FFI bindings to KVM generated using bindgen - feature "vmm-sys-util" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(vmm-sys-util-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/fam-wrappers) = %{version}
Provides:       crate(%{pkgname}/vmm-sys-util) = %{version}

%description -n %{name}+vmm-sys-util
This metapackage enables feature "vmm-sys-util" for the Rust kvm-bindings crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fam-wrappers" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
