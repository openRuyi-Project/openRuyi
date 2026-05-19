# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_str_bytes
%global full_version 7.1.1
%global pkgname os-str-bytes-7.0

Name:           rust-os-str-bytes-7.0
Version:        7.1.1
Release:        %autorelease
Summary:        Rust crate "os_str_bytes"
License:        MIT OR Apache-2.0
URL:            https://github.com/dylni/os_str_bytes
#!RemoteAsset:  sha256:63eceb7b5d757011a87d08eb2123db15d87fb0c281f65d101ce30a1e96c3ad5c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/checked-conversions)
Provides:       crate(%{pkgname}/conversions)
Provides:       crate(%{pkgname}/raw-os-str)

%description
Source code for takopackized Rust crate "os_str_bytes"

%package     -n %{name}+default
Summary:        Lossless functionality for platform-native strings - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/memchr)
Requires:       crate(%{pkgname}/raw-os-str)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Lossless functionality for platform-native strings - feature "memchr"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/default) >= 2.8.0
Provides:       crate(%{pkgname}/memchr)

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
