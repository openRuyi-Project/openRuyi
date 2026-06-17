# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name redox_syscall
%global full_version 0.8.0
%global pkgname redox-syscall-0.8

Name:           rust-redox-syscall-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "redox_syscall"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/syscall
#!RemoteAsset:  sha256:7c7591fa2c6b601dfcfe5f043f65a1c39fcdf50efefcd7f1572e538c1f4b398d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/core) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/userspace) = %{version}

%description
Source code for takopackized Rust crate "redox_syscall"

%package     -n %{name}+rustc-dep-of-std
Summary:        Access raw Redox system calls - feature "rustc-dep-of-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/core) = %{version}
Requires:       crate(bitflags-2/rustc-dep-of-std) >= 2.4.0
Provides:       crate(%{pkgname}/rustc-dep-of-std) = %{version}

%description -n %{name}+rustc-dep-of-std
This metapackage enables feature "rustc-dep-of-std" for the Rust redox_syscall crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
