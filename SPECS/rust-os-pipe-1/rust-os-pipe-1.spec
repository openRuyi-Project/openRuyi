# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_pipe
%global full_version 1.2.3
%global pkgname os-pipe-1

Name:           rust-os-pipe-1
Version:        1.2.3
Release:        %autorelease
Summary:        Rust crate "os_pipe"
License:        MIT
URL:            https://github.com/oconnor663/os_pipe.rs
#!RemoteAsset:  sha256:7d8fae84b431384b68627d0f9b3b1245fcf9f46f6c0e3dc902e9dce64edd1967
Source:         https://static.crates.io/crates/os_pipe/1.2.3/download#/rust-os-pipe-1-1.2.3.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.62
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "os_pipe"

%package     -n %{name}+default
Summary:        Cross-platform library for opening OS pipes - feature "default" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/io-safety) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust os_pipe crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "io_safety" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
