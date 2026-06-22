# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name redb
%global full_version 3.1.3
%global pkgname redb-3

Name:           rust-redb-3
Version:        3.1.3
Release:        %autorelease
Summary:        Rust crate "redb"
License:        MIT OR Apache-2.0
URL:            https://www.redb.org
#!RemoteAsset:  sha256:4ba239c1c1693315d3cc0e601db3b3965543afbf48c41730fdca2f069f510f4a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.174
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cache-metrics) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "redb"

%package     -n %{name}+chrono-v0-4
Summary:        Rust Embedded DataBase - feature "chrono_v0_4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.41
Provides:       crate(%{pkgname}/chrono-v0-4) = %{version}

%description -n %{name}+chrono-v0-4
This metapackage enables feature "chrono_v0_4" for the Rust redb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Rust Embedded DataBase - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.17
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust redb crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid
Summary:        Rust Embedded DataBase - feature "uuid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1/default) >= 1.17.0
Provides:       crate(%{pkgname}/uuid) = %{version}

%description -n %{name}+uuid
This metapackage enables feature "uuid" for the Rust redb crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
