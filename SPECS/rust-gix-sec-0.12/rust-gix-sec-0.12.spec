# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-sec
%global full_version 0.12.2
%global pkgname gix-sec-0.12

Name:           rust-gix-sec-0.12
Version:        0.12.2
Release:        %autorelease
Summary:        Rust crate "gix-sec"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:ea9962ed6d9114f7f100efe038752f41283c225bb507a2888903ac593dffa6be
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(gix-path-0.10/default) >= 0.10.21
Requires:       crate(libc-0.2/default) >= 0.2.176
Requires:       crate(windows-sys-0.61/default) >= 0.61.1
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.1
Requires:       crate(windows-sys-0.61/win32-security-authorization) >= 0.61.1
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.1
Requires:       crate(windows-sys-0.61/win32-system-memory) >= 0.61.1
Requires:       crate(windows-sys-0.61/win32-system-threading) >= 0.61.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-sec"

%package     -n %{name}+document-features
Summary:        The gitoxide project providing a shared trust model - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-sec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project providing a shared trust model - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/serde) >= 2.0.0
Requires:       crate(serde-1/derive) >= 1.0.114
Requires:       crate(serde-1/std) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-sec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
