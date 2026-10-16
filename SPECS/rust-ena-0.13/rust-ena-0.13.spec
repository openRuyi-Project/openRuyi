# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ena
%global full_version 0.13.1
%global pkgname ena-0.13

Name:           rust-ena-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "ena"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang-nursery/ena
#!RemoteAsset:  sha256:8944dc8fa28ce4a38f778bd46bf7d923fe73eed5a439398507246c8e017e6f36
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

%package     -n %{name}+petgraph
Summary:        Union-find, congruence closure, and other unification code - feature "petgraph" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(petgraph-0.4/default) >= 0.4.5
Provides:       crate(%{pkgname}/congruence-closure) = %{version}
Provides:       crate(%{pkgname}/petgraph) = %{version}

%description -n %{name}+petgraph
Based on code from rustc.
This metapackage enables feature "petgraph" for the Rust ena crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "congruence-closure" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
