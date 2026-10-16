# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smartstring
%global full_version 1.0.1
%global pkgname smartstring-1

Name:           rust-smartstring-1
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

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(static-assertions-1/default) >= 1.0.0
Requires:       crate(version-check-0.9) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "smartstring"

%package     -n %{name}+arbitrary
Summary:        Compact inlined strings - feature "arbitrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary) = %{version}

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust smartstring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proptest
Summary:        Compact inlined strings - feature "proptest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proptest-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/proptest) = %{version}

%description -n %{name}+proptest
This metapackage enables feature "proptest" for the Rust smartstring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Compact inlined strings - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust smartstring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test
Summary:        Compact inlined strings - feature "test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arbitrary) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(arbitrary-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/test) = %{version}

%description -n %{name}+test
This metapackage enables feature "test" for the Rust smartstring crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
