# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name linux-loader
%global full_version 0.13.2
%global pkgname linux-loader-0.13

Name:           rust-linux-loader-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "linux-loader"
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/rust-vmm/linux-loader
#!RemoteAsset:  sha256:de72cb02c55ecffcf75fe78295926f872eb6eb0a58d629c58a8c324dc26380f6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(vm-memory-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bzimage) = %{version}
Provides:       crate(%{pkgname}/elf) = %{version}
Provides:       crate(%{pkgname}/pe) = %{version}

%description
Source code for takopackized Rust crate "linux-loader"

%package     -n %{name}+default
Summary:        Linux kernel image loading crate - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/elf) = %{version}
Requires:       crate(%{pkgname}/pe) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust linux-loader crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
