# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dissimilar
%global full_version 1.0.10
%global pkgname dissimilar-1

Name:           rust-dissimilar-1
Version:        1.0.10
Release:        %autorelease
Summary:        Rust crate "dissimilar"
License:        Apache-2.0
URL:            https://github.com/dtolnay/dissimilar
#!RemoteAsset:  sha256:8975ffdaa0ef3661bfe02dbdcc06c9f829dfafe6a3c474de366a8d5e44276921
Source:         https://static.crates.io/crates/dissimilar/1.0.10/download#/rust-dissimilar-1-1.0.10.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "dissimilar"

%package     -n %{name}+default
Summary:        Diff library with semantic cleanup, based on Google's diff-match-patch - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust dissimilar crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
