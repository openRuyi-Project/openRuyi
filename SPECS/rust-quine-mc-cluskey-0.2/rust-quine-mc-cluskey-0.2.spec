# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quine-mc_cluskey
%global full_version 0.2.4
%global pkgname quine-mc-cluskey-0.2

Name:           rust-quine-mc-cluskey-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "quine-mc_cluskey"
License:        MIT
URL:            https://github.com/oli-obk/quine-mc_cluskey
#!RemoteAsset:  sha256:07589615d719a60c8dd8a4622e7946465dfef20d1a428f969e3443e7386d5f45
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "quine-mc_cluskey"

%package     -n %{name}+quickcheck
Summary:        The Quine-McCluskey algorithm and Petrick's method - feature "quickcheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quickcheck-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/quickcheck) = %{version}

%description -n %{name}+quickcheck
This metapackage enables feature "quickcheck" for the Rust quine-mc_cluskey crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
