# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name histo
%global full_version 1.0.0
%global pkgname histo-1

Name:           rust-histo-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "histo"
License:        Apache-2.0 OR MIT
URL:            https://github.com/fitzgen/histo
#!RemoteAsset:  sha256:a6a96a1c8acf372eefef3b065d800986a6d11abdc2c27cc61255513646b3df6c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(streaming-stats-0.1/default) >= 0.1.28

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "histo"

%package     -n %{name}+quickcheck
Summary:        Simple histograms with configurable buckets - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust histo crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
