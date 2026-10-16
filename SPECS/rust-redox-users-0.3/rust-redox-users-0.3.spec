# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name redox_users
%global full_version 0.3.5
%global pkgname redox-users-0.3

Name:           rust-redox-users-0.3
Version:        0.3.5
Release:        %autorelease
Summary:        Rust crate "redox_users"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/users
#!RemoteAsset:  sha256:de0737333e7a9502c789a36d7c7fa6092a49895d4faa31ca5df163857ded2e9d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.1/default) >= 0.1.0
Requires:       crate(redox-syscall-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "redox_users"

%package     -n %{name}+rust-argon2
Summary:        Access Redox users and groups functionality - feature "rust-argon2" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-argon2-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/auth) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rust-argon2) = %{version}

%description -n %{name}+rust-argon2
This metapackage enables feature "rust-argon2" for the Rust redox_users crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "auth", and "default" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
