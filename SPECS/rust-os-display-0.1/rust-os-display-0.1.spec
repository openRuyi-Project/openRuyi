# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_display
%global full_version 0.1.3
%global pkgname os-display-0.1

Name:           rust-os-display-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "os_display"
License:        MIT
URL:            https://github.com/blyxxyz/os_display
#!RemoteAsset:  sha256:7a6229bad892b46b0dcfaaeb18ad0d2e56400f5aaea05b768bde96e73676cf75
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-width-0.1/default) >= 0.1.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/native) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unix) = %{version}
Provides:       crate(%{pkgname}/windows) = %{version}

%description
Source code for takopackized Rust crate "os_display"

%package     -n %{name}+default
Summary:        Display strings in a safe platform-appropriate way - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/native) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust os_display
crate, by pulling in any additional dependencies needed by that feature.

%prep -a
# Cargo ships the original manifest as a backup.
rm -f Cargo.toml.orig

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
