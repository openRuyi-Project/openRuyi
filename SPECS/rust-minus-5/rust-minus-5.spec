# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name minus
%global full_version 5.6.1
%global pkgname minus-5

Name:           rust-minus-5
Version:        5.6.1
Release:        %autorelease
Summary:        Rust crate "minus"
License:        MIT OR Apache-2.0
URL:            https://github.com/arijit79/minus
#!RemoteAsset:  sha256:093bd0520d2a37943566a73750e6d44094dac75d66a978d1f0d97ffc78686832
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Requires:       crate(crossterm-0.27/default) >= 0.27.0
Requires:       crate(once-cell-1/default) >= 1.18.0
Requires:       crate(once-cell-1/parking-lot) >= 1.18.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.1
Requires:       crate(textwrap-0.16/unicode-width) >= 0.16.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dynamic-output) = %{version}
Provides:       crate(%{pkgname}/static-output) = %{version}

%description
Source code for takopackized Rust crate "minus"

%package     -n %{name}+regex
Summary:        Asynchronous data feedable terminal paging library for Rust - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/regex) = %{version}
Provides:       crate(%{pkgname}/search) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust minus crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "search" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
