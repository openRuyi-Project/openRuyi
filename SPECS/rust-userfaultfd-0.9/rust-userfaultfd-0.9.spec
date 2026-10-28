# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name userfaultfd
%global full_version 0.9.0
%global pkgname userfaultfd-0.9

Name:           rust-userfaultfd-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "userfaultfd"
License:        MIT OR Apache-2.0
URL:            https://github.com/bytecodealliance/userfaultfd-rs
#!RemoteAsset:  sha256:5b3a8a0cb358f7d1b7ee9b6784be122b6f51248a6d9e214d555beb9b44c72aea
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.65
Requires:       crate(nix-0.27/default) >= 0.27.0
Requires:       crate(nix-0.27/ioctl) >= 0.27.0
Requires:       crate(thiserror-1/default) >= 1.0.4
Requires:       crate(userfaultfd-sys-0.6/default) >= 0.6.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "userfaultfd"

%package     -n %{name}+linux4-14
Summary:        Rust bindings for the Linux userfaultfd functionality - feature "linux4_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nix-0.27/ioctl) >= 0.27.0
Requires:       crate(nix-0.27/process) >= 0.27.0
Requires:       crate(userfaultfd-sys-0.6/linux4-14) >= 0.6.0
Provides:       crate(%{pkgname}/linux4-14) = %{version}

%description -n %{name}+linux4-14
This metapackage enables feature "linux4_14" for the Rust userfaultfd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+linux5-13
Summary:        Rust bindings for the Linux userfaultfd functionality - feature "linux5_13"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(userfaultfd-sys-0.6/linux5-13) >= 0.6.0
Provides:       crate(%{pkgname}/linux5-13) = %{version}

%description -n %{name}+linux5-13
This metapackage enables feature "linux5_13" for the Rust userfaultfd crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+linux5-7
Summary:        Rust bindings for the Linux userfaultfd functionality - feature "linux5_7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(userfaultfd-sys-0.6/linux5-7) >= 0.6.0
Provides:       crate(%{pkgname}/linux5-7) = %{version}

%description -n %{name}+linux5-7
This metapackage enables feature "linux5_7" for the Rust userfaultfd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
