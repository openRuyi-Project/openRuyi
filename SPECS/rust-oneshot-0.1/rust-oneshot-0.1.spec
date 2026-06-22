# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name oneshot
%global full_version 0.1.13
%global pkgname oneshot-0.1

Name:           rust-oneshot-0.1
Version:        0.1.13
Release:        %autorelease
Summary:        Rust crate "oneshot"
License:        MIT OR Apache-2.0
URL:            https://github.com/faern/oneshot
#!RemoteAsset:  sha256:269bca4c2591a28585d6bf10d9ed0332b7d76900a1b02bec41bdc3a2cdcda107
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "oneshot"

%package     -n %{name}+default
Summary:        Oneshot spsc channel with (potentially) lock-free non-blocking send, and a receiver supporting both thread blocking receive operations as well as Future based async polling - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust oneshot crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loom
Summary:        Oneshot spsc channel with (potentially) lock-free non-blocking send, and a receiver supporting both thread blocking receive operations as well as Future based async polling - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(loom-0.7/default) >= 0.7.2
Requires:       crate(loom-0.7/futures) >= 0.7.2
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust oneshot crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
