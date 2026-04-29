# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core-foundation
%global full_version 0.10.1
%global pkgname core-foundation-0.10

Name:           rust-core-foundation-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "core-foundation"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/core-foundation-rs
#!RemoteAsset:  sha256:b2a6cd9ae233e7f62ba4e9353e81a88df7fc8a5987b8d445b4d90c879bd156f6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(core-foundation-sys-0.8) >= 0.8.7
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "core-foundation"

%package     -n %{name}+link
Summary:        Bindings to Core Foundation for macOS - feature "link" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(core-foundation-sys-0.8/link) >= 0.8.7
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/link)

%description -n %{name}+link
This metapackage enables feature "link" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+mac-os-10-7-support
Summary:        Bindings to Core Foundation for macOS - feature "mac_os_10_7_support"
Requires:       crate(%{pkgname})
Requires:       crate(core-foundation-sys-0.8/mac-os-10-7-support) >= 0.8.7
Provides:       crate(%{pkgname}/mac-os-10-7-support)

%description -n %{name}+mac-os-10-7-support
This metapackage enables feature "mac_os_10_7_support" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mac-os-10-8-features
Summary:        Bindings to Core Foundation for macOS - feature "mac_os_10_8_features"
Requires:       crate(%{pkgname})
Requires:       crate(core-foundation-sys-0.8/mac-os-10-8-features) >= 0.8.7
Provides:       crate(%{pkgname}/mac-os-10-8-features)

%description -n %{name}+mac-os-10-8-features
This metapackage enables feature "mac_os_10_8_features" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-uuid
Summary:        Bindings to Core Foundation for macOS - feature "with-uuid"
Requires:       crate(%{pkgname})
Requires:       crate(uuid-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/with-uuid)

%description -n %{name}+with-uuid
This metapackage enables feature "with-uuid" for the Rust core-foundation crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
