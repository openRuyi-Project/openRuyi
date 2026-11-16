# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name which
%global full_version 5.0.0
%global pkgname which-5

Name:           rust-which-5
Version:        5.0.0
Release:        %autorelease
Summary:        Rust crate "which"
License:        MIT
URL:            https://github.com/harryfei/which-rs.git
#!RemoteAsset:  sha256:9bf3ea8596f3a0dd5980b46430f2058dfe2c36a27ccfbb1845d6fbfcd9ba6e14
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1/default) >= 1.6.1
Requires:       crate(home-0.5/default) >= 0.5.5
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(rustix-0.38/fs) >= 0.38.10
Requires:       crate(rustix-0.38/std) >= 0.38.10
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-foundation) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-storage-filesystem) >= 0.48.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Locate installed executable in cross platforms.
Source code for takopackized Rust crate "which"

%package     -n %{name}+regex
Summary:        Rust equivalent of Unix command "which" - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.9.6
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
Locate installed executable in cross platforms.
This metapackage enables feature "regex" for the Rust which crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
