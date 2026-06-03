# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smartstring
%global full_version 1.0.1
%global pkgname smartstring-1.0

Name:           rust-smartstring-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "smartstring"
License:        MPL-2.0+
URL:            https://github.com/bodil/smartstring
#!RemoteAsset:  sha256:3fb72c633efbaa2dd666986505016c32c3044395ceaf881518399d2f4127ee29
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1.0/default) >= 1.5.0
Requires:       crate(static-assertions-1.0/default) >= 1.1.0
Requires:       crate(version-check-0.9/default) >= 0.9.5
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "smartstring"

%package     -n %{name}+serde
Summary:        Compact inlined strings - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust smartstring crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
