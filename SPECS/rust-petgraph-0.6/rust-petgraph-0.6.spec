# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name petgraph
%global full_version 0.6.5
%global pkgname petgraph-0.6

Name:           rust-petgraph-0.6
Version:        0.6.5
Release:        %autorelease
Summary:        Rust crate "petgraph"
License:        MIT OR Apache-2.0
URL:            https://github.com/petgraph/petgraph
#!RemoteAsset:  sha256:b4c5cc86750666a3ed20bdaf5ca2a0344f9c67674cae0515bec2da16fbaa47db
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fixedbitset-0.4) >= 0.4.0
Requires:       crate(indexmap-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/generate) = %{version}
Provides:       crate(%{pkgname}/graphmap) = %{version}
Provides:       crate(%{pkgname}/matrix-graph) = %{version}
Provides:       crate(%{pkgname}/stable-graph) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Provides graph types and graph algorithms.
Source code for takopackized Rust crate "petgraph"

%package     -n %{name}+all
Summary:        Graph data structure library - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/graphmap) = %{version}
Requires:       crate(%{pkgname}/matrix-graph) = %{version}
Requires:       crate(%{pkgname}/quickcheck) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/stable-graph) = %{version}
Requires:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
Provides graph types and graph algorithms.
This metapackage enables feature "all" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Graph data structure library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/graphmap) = %{version}
Requires:       crate(%{pkgname}/matrix-graph) = %{version}
Requires:       crate(%{pkgname}/stable-graph) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Provides graph types and graph algorithms.
This metapackage enables feature "default" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quickcheck
Summary:        Graph data structure library - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
Provides graph types and graph algorithms.
This metapackage enables feature "quickcheck" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Graph data structure library - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/rayon) >= 2.0.0
Requires:       crate(rayon-1/default) >= 1.5.3
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
Provides graph types and graph algorithms.
This metapackage enables feature "rayon" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Graph data structure library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
Provides graph types and graph algorithms.
This metapackage enables feature "serde" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-1
Summary:        Graph data structure library - feature "serde-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Provides:       crate(%{pkgname}/serde-1) = %{version}

%description -n %{name}+serde-1
Provides graph types and graph algorithms.
This metapackage enables feature "serde-1" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Graph data structure library - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
Provides graph types and graph algorithms.
This metapackage enables feature "serde_derive" for the Rust petgraph crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
