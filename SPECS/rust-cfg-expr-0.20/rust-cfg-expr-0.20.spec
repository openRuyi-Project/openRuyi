# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cfg-expr
%global full_version 0.20.8
%global pkgname cfg-expr-0.20

Name:           rust-cfg-expr-0.20
Version:        0.20.8
Release:        %autorelease
Summary:        Rust crate "cfg-expr"
License:        MIT OR Apache-2.0
URL:            https://github.com/EmbarkStudios/cfg-expr
#!RemoteAsset:  sha256:fb693542bcafa528e198be0ebd9d3632ca5b7c93dbe7237460e199910835997c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1/default) >= 1.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cfg-expr"

%package     -n %{name}+target-lexicon
Summary:        Parser and evaluator for Rust `cfg()` expressions - feature "target-lexicon" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(target-lexicon-0.13/default) >= 0.13.5
Provides:       crate(%{pkgname}/target-lexicon) = %{version}
Provides:       crate(%{pkgname}/targets) = %{version}

%description -n %{name}+target-lexicon
This metapackage enables feature "target-lexicon" for the Rust cfg-expr crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "targets" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
