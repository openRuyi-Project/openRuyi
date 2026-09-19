# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_str_bytes
%global full_version 7.2.0
%global pkgname os-str-bytes-7

Name:           rust-os-str-bytes-7
Version:        7.2.0
Release:        %autorelease
Summary:        Rust crate "os_str_bytes"
License:        MIT OR Apache-2.0
URL:            https://github.com/dylni/os_str_bytes
#!RemoteAsset:  sha256:89284d0c2af7b0eb5e814798aa07265413c8fd72009f7fc82ea25a81fb287ce9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/checked-conversions) = %{version}
Provides:       crate(%{pkgname}/conversions) = %{version}
Provides:       crate(%{pkgname}/raw-os-str) = %{version}

%description
Source code for takopackized Rust crate "os_str_bytes"

%package     -n %{name}+default
Summary:        Lossless functionality for platform-native strings - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/memchr) = %{version}
Requires:       crate(%{pkgname}/raw-os-str) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Lossless functionality for platform-native strings - feature "memchr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/default) >= 2.3.5
Provides:       crate(%{pkgname}/memchr) = %{version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
