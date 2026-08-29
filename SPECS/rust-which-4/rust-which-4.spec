# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name which
%global full_version 4.4.2
%global pkgname which-4

Name:           rust-which-4
Version:        4.4.2
Release:        %autorelease
Summary:        Rust crate "which"
License:        MIT
URL:            https://github.com/harryfei/which-rs.git
#!RemoteAsset:  sha256:87ba24419a2078cd2b0f2ede2691b6c66d8e47836da3b6db8265ebad47afbfc7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(either-1/default) >= 1.6.1
Requires:       crate(home-0.5/default) >= 0.5.5
Requires:       crate(once-cell-1/default) >= 1.0.0
Requires:       crate(rustix-0.38/fs) >= 0.38.10
Requires:       crate(rustix-0.38/std) >= 0.38.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Locate installed executable in cross platforms.
Source code for takopackized Rust crate "which"

%package     -n %{name}+regex
Summary:        Rust equivalent of Unix command "which" - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.5.5
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
Locate installed executable in cross platforms.
This metapackage enables feature "regex" for the Rust which crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
