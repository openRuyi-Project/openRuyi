# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uzers
%global full_version 0.12.2
%global pkgname uzers-0.12

Name:           rust-uzers-0.12
Version:        0.12.2
Release:        %autorelease
Summary:        Rust crate "uzers"
License:        MIT
URL:            https://github.com/rustadopt/uzers-rs
#!RemoteAsset:  sha256:0b8275fb1afee25b4111d2dc8b5c505dbbc4afd0b990cb96deb2d88bff8be18d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cache) = %{version}
Provides:       crate(%{pkgname}/mock) = %{version}
Provides:       crate(%{pkgname}/test-integration) = %{version}

%description
Source code for takopackized Rust crate "uzers"

%package     -n %{name}+default
Summary:        Continuation of users, a library for accessing Unix users and groups - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cache) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(%{pkgname}/mock) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust uzers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Continuation of users, a library for accessing Unix users and groups - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust uzers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
