# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name redox_users
%global full_version 0.5.2
%global pkgname redox-users-0.5

Name:           rust-redox-users-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "redox_users"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/users
#!RemoteAsset:  sha256:a4e608c6638b9c18977b00b475ac1f28d14e84b27d8d42f70e0bf1e3dec127ac
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.2/default) >= 0.2.16
Requires:       crate(getrandom-0.2/std) >= 0.2.16
Requires:       crate(libredox-0.1/call) >= 0.1.10
Requires:       crate(libredox-0.1/std) >= 0.1.10
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "redox_users"

%package     -n %{name}+auth
Summary:        Access Redox users and groups functionality - feature "auth" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rust-argon2)
Requires:       crate(%{pkgname}/zeroize)
Provides:       crate(%{pkgname}/auth)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+auth
This metapackage enables feature "auth" for the Rust redox_users crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+rust-argon2
Summary:        Access Redox users and groups functionality - feature "rust-argon2"
Requires:       crate(%{pkgname})
Requires:       crate(rust-argon2-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/rust-argon2)

%description -n %{name}+rust-argon2
This metapackage enables feature "rust-argon2" for the Rust redox_users crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Access Redox users and groups functionality - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0/default) >= 1.4
Requires:       crate(zeroize-1.0/zeroize-derive) >= 1.4
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust redox_users crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
