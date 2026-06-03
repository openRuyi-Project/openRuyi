# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name redox_users
%global full_version 0.4.6
%global pkgname redox-users-0.4

Name:           rust-redox-users-0.4
Version:        0.4.6
Release:        %autorelease
Summary:        Rust crate "redox_users"
License:        MIT
URL:            https://gitlab.redox-os.org/redox-os/users
#!RemoteAsset:  sha256:ba009ff324d1fc1b900bd1fdb31564febe58a8ccc8a6fdbb93b543d33b13ca43
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.2/default) >= 0.2.16
Requires:       crate(getrandom-0.2/std) >= 0.2.16
Requires:       crate(libredox-0.1/call) >= 0.1.12
Requires:       crate(libredox-0.1/std) >= 0.1.12
Requires:       crate(thiserror-1.0/default) >= 1.0.69
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "redox_users"

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
