# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name which
%global full_version 6.0.3
%global pkgname which-6

Name:           rust-which-6
Version:        6.0.3
Release:        %autorelease
Summary:        Rust crate "which"
License:        MIT
URL:            https://github.com/harryfei/which-rs.git
#!RemoteAsset:  sha256:b4ee928febd44d98f2f459a4a79bd4d928591333a494a10a868418ac1b39cf1f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1/default) >= 1.9.0
Requires:       crate(home-0.5/default) >= 0.5.9
Requires:       crate(rustix-0.38/fs) >= 0.38.30
Requires:       crate(rustix-0.38/std) >= 0.38.30
Requires:       crate(winsafe-0.0.19/default) >= 0.0.19
Requires:       crate(winsafe-0.0.19/kernel) >= 0.0.19

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Locate installed executable in cross platforms.
Source code for takopackized Rust crate "which"

%package     -n %{name}+regex
Summary:        Rust equivalent of Unix command "which" - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.10.2
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
Locate installed executable in cross platforms.
This metapackage enables feature "regex" for the Rust which crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Rust equivalent of Unix command "which" - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1) >= 0.1.40
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
Locate installed executable in cross platforms.
This metapackage enables feature "tracing" for the Rust which crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
