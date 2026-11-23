# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clircle
%global full_version 0.6.1
%global pkgname clircle-0.6

Name:           rust-clircle-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "clircle"
License:        MIT OR Apache-2.0
URL:            https://github.com/niklasmohrin/clircle
#!RemoteAsset:  sha256:7d9334f725b46fb9bed8580b9b47a932587e044fadb344ed7fa98774b067ac1a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(windows-0.56/default) >= 0.56.0
Requires:       crate(windows-0.56/win32-storage-filesystem) >= 0.56.0
Requires:       crate(windows-0.56/win32-system-console) >= 0.56.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/test-close-again) = %{version}

%description
Source code for takopackized Rust crate "clircle"

%package     -n %{name}+serde
Summary:        Detect IO circles in your CLI apps arguments - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.117
Requires:       crate(serde-derive-1/default) >= 1.0.117
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust clircle crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
