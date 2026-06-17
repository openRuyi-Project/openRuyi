# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name peg
%global full_version 0.8.5
%global pkgname peg-0.8

Name:           rust-peg-0.8
Version:        0.8.5
Release:        %autorelease
Summary:        Rust crate "peg"
License:        MIT
URL:            https://github.com/kevinmehall/rust-peg
#!RemoteAsset:  sha256:9928cfca101b36ec5163e70049ee5368a8a1c3c6efc9ca9c5f9cc2f816152477
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(peg-macros-0.8/default) >= 0.8.5
Requires:       crate(peg-runtime-0.8/default) >= 0.8.5
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "peg"

%package     -n %{name}+std
Summary:        Simple Parsing Expression Grammar (PEG) parser generator - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(peg-runtime-0.8/std) >= 0.8.5
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust peg crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+trace
Summary:        Simple Parsing Expression Grammar (PEG) parser generator - feature "trace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(peg-macros-0.8/trace) >= 0.8.5
Provides:       crate(%{pkgname}/trace) = %{version}

%description -n %{name}+trace
This metapackage enables feature "trace" for the Rust peg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Simple Parsing Expression Grammar (PEG) parser generator - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(peg-runtime-0.8/unstable) >= 0.8.5
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust peg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
