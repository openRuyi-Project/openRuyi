# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name portable-atomic
%global full_version 1.13.1
%global pkgname portable-atomic-1

Name:           rust-portable-atomic-1
Version:        1.13.1
Release:        %autorelease
Summary:        Rust crate "portable-atomic"
License:        Apache-2.0 OR MIT
URL:            https://github.com/taiki-e/portable-atomic
#!RemoteAsset:  sha256:c33a9471896f1c69cecef8d20cbe2f7accd12527ce60845ff44c153bb2a21b49
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/disable-fiq) = %{version}
Provides:       crate(%{pkgname}/fallback) = %{version}
Provides:       crate(%{pkgname}/float) = %{version}
Provides:       crate(%{pkgname}/force-amo) = %{version}
Provides:       crate(%{pkgname}/require-cas) = %{version}
Provides:       crate(%{pkgname}/s-mode) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unsafe-assume-privileged) = %{version}
Provides:       crate(%{pkgname}/unsafe-assume-single-core) = %{version}

%description
Source code for takopackized Rust crate "portable-atomic"

%package     -n %{name}+critical-section
Summary:        Portable atomic types including support for 128-bit atomics, atomic float, etc - feature "critical-section"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(critical-section-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/critical-section) = %{version}

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust portable-atomic crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Portable atomic types including support for 128-bit atomics, atomic float, etc - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.60
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust portable-atomic crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
