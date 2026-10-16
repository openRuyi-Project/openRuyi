# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name roadmap
%global full_version 0.7.0
%global pkgname roadmap-0.7

Name:           rust-roadmap-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "roadmap"
License:        MIT-0
URL:            https://gitlab.com/larswirzenius/roadmap
#!RemoteAsset:  sha256:ec49775c5134c7e4befdedecaf112bb72964baa9b24bedfc79b54c3ca0ee9f77
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(marked-yaml-0.7/default) >= 0.7.0
Requires:       crate(marked-yaml-0.7/serde-path) >= 0.7.0
Requires:       crate(serde-1/default) >= 1.0.134
Requires:       crate(serde-1/derive) >= 1.0.134
Requires:       crate(tempfile-3/default) >= 3.10.0
Requires:       crate(textwrap-0.16/default) >= 0.16.1
Requires:       crate(thiserror-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "roadmap"

%package     -n %{name}+bin
Summary:        Model a project roadmap as a directed acyclic graph - feature "bin" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.5.1
Requires:       crate(clap-4/derive) >= 4.5.1
Provides:       crate(%{pkgname}/bin) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+bin
This metapackage enables feature "bin" for the Rust roadmap crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
