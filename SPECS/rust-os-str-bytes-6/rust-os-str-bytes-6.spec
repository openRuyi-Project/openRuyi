# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name os_str_bytes
%global full_version 6.6.1
%global pkgname os-str-bytes-6

Name:           rust-os-str-bytes-6
Version:        6.6.1
Release:        %autorelease
Summary:        Rust crate "os_str_bytes"
License:        MIT OR Apache-2.0
URL:            https://github.com/dylni/os_str_bytes
#!RemoteAsset:  sha256:e2355d85b9a3786f481747ced0e0ff2ba35213a1f9bd406ed906554d7af805a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/checked-conversions) = %{version}
Provides:       crate(%{pkgname}/conversions) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}
Provides:       crate(%{pkgname}/raw-os-str) = %{version}

%description
Source code for takopackized Rust crate "os_str_bytes"

%package     -n %{name}+default
Summary:        Convert between byte sequences and platform-native strings - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/memchr) = %{version}
Requires:       crate(%{pkgname}/raw-os-str) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Convert between byte sequences and platform-native strings - feature "memchr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/memchr) = %{version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+print-bytes
Summary:        Convert between byte sequences and platform-native strings - feature "print_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(print-bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/print-bytes) = %{version}

%description -n %{name}+print-bytes
This metapackage enables feature "print_bytes" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uniquote
Summary:        Convert between byte sequences and platform-native strings - feature "uniquote"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uniquote-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/uniquote) = %{version}

%description -n %{name}+uniquote
This metapackage enables feature "uniquote" for the Rust os_str_bytes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
