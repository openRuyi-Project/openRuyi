# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ena
%global full_version 0.14.4
%global pkgname ena-0.14

Name:           rust-ena-0.14
Version:        0.14.4
Release:        %autorelease
Summary:        Rust crate "ena"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/ena
#!RemoteAsset:  sha256:eabffdaee24bd1bf95c5ef7cec31260444317e72ea56c4c91750e8b7ee58d5f1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/bench) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Based on code from rustc.
Source code for takopackized Rust crate "ena"

%package     -n %{name}+dogged
Summary:        Union-find, congruence closure, and other unification code - feature "dogged" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dogged-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/dogged) = %{version}
Provides:       crate(%{pkgname}/persistent) = %{version}

%description -n %{name}+dogged
Based on code from rustc.
This metapackage enables feature "dogged" for the Rust ena crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "persistent" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
