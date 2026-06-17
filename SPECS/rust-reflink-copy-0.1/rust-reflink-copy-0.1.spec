# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name reflink-copy
%global full_version 0.1.29
%global pkgname reflink-copy-0.1

Name:           rust-reflink-copy-0.1
Version:        0.1.29
Release:        %autorelease
Summary:        Rust crate "reflink-copy"
License:        MIT OR Apache-2.0
URL:            https://github.com/cargo-bins/reflink-copy
#!RemoteAsset:  sha256:13362233b147e57674c37b802d216b7c5e3dcccbed8967c84f0d8d223868ae27
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:         0001-fix-dependency-ranges.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.169
Requires:       crate(rustix-1/fs) >= 1.0.1
Requires:       crate(rustix-1/std) >= 1.0.1
Requires:       crate(windows-0.62/default) >= 0.62.2
Requires:       crate(windows-0.62/win32-foundation) >= 0.62.2
Requires:       crate(windows-0.62/win32-storage-filesystem) >= 0.62.2
Requires:       crate(windows-0.62/win32-system-io) >= 0.62.2
Requires:       crate(windows-0.62/win32-system-ioctl) >= 0.62.2
Requires:       crate(windows-0.62/win32-system-systemservices) >= 0.62.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "reflink-copy"

%package     -n %{name}+tracing
Summary:        Copy-on-write mechanism on supported file systems - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.37
Requires:       crate(tracing-attributes-0.1/default) >= 0.1.26
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust reflink-copy crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
