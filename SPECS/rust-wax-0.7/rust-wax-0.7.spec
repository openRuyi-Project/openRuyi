# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wax
%global full_version 0.7.0
%global pkgname wax-0.7

Name:           rust-wax-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "wax"
License:        MIT
URL:            https://github.com/olson-sean-k/wax
#!RemoteAsset:  sha256:1f8cbf8125142b9b30321ac8721f54c52fbcd6659f76cf863d5e2e38c07a3d7b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-format-0.2/default) >= 0.2.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(nom-7/default) >= 7.0.0
Requires:       crate(pori-0.0.0/default) >= 0.0.0
Requires:       crate(regex-1/perf) >= 1.12.0
Requires:       crate(regex-1/std) >= 1.12.0
Requires:       crate(regex-1/unicode-case) >= 1.12.0
Requires:       crate(thiserror-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "wax"

%package     -n %{name}+miette
Summary:        Opinionated and portable globs that can be matched against paths and directory trees - feature "miette"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(miette-5) >= 5.10.0
Requires:       crate(tardar-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/miette) = %{version}

%description -n %{name}+miette
This metapackage enables feature "miette" for the Rust wax crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walk
Summary:        Opinionated and portable globs that can be matched against paths and directory trees - feature "walk" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(walkdir-2/default) >= 2.5.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/walk) = %{version}

%description -n %{name}+walk
This metapackage enables feature "walk" for the Rust wax crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
