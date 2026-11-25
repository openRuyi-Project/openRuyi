# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name daggy
%global full_version 0.9.0
%global pkgname daggy-0.9

Name:           rust-daggy-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "daggy"
License:        MIT OR Apache-2.0
URL:            https://github.com/mitchmindtree/daggy
#!RemoteAsset:  sha256:804169db156b21258a2545757336922d93dfa229892c75911a0ad141aa0ff241
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(petgraph-0.8) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
It is Implemented on top of petgraph's Graph data structure and attempts to follow similar conventions where suitable.
Source code for takopackized Rust crate "daggy"

%package     -n %{name}+serde
Summary:        Directed acyclic graph data structure library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
It is Implemented on top of petgraph's Graph data structure and attempts to follow similar conventions where suitable.
This metapackage enables feature "serde" for the Rust daggy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-1
Summary:        Directed acyclic graph data structure library - feature "serde-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(petgraph-0.8/serde-1) >= 0.8.0
Provides:       crate(%{pkgname}/serde-1) = %{version}

%description -n %{name}+serde-1
It is Implemented on top of petgraph's Graph data structure and attempts to follow similar conventions where suitable.
This metapackage enables feature "serde-1" for the Rust daggy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable-dag
Summary:        Directed acyclic graph data structure library - feature "stable_dag"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(petgraph-0.8/stable-graph) >= 0.8.0
Provides:       crate(%{pkgname}/stable-dag) = %{version}

%description -n %{name}+stable-dag
It is Implemented on top of petgraph's Graph data structure and attempts to follow similar conventions where suitable.
This metapackage enables feature "stable_dag" for the Rust daggy crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
