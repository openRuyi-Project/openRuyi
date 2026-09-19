# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name print_bytes
%global full_version 2.0.0
%global pkgname print-bytes-2

Name:           rust-print-bytes-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "print_bytes"
License:        MIT OR Apache-2.0
URL:            https://github.com/dylni/print_bytes
#!RemoteAsset:  sha256:f45cdf97bdb7d71eda10cfc440f03a2523eee693f128fab26f18428625a1cf81
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-console) >= 0.52.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/specialization) = %{version}

%description
Source code for takopackized Rust crate "print_bytes"

%package     -n %{name}+os-str-bytes
Summary:        Print bytes as losslessly as possible - feature "os_str_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(os-str-bytes-7) >= 7.0.0
Provides:       crate(%{pkgname}/os-str-bytes) = %{version}

%description -n %{name}+os-str-bytes
This metapackage enables feature "os_str_bytes" for the Rust print_bytes crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-APACHE
%license LICENSE-MIT
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
