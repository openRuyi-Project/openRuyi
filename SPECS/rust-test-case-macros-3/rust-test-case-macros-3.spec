# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name test-case-macros
%global full_version 3.3.1
%global pkgname test-case-macros-3

Name:           rust-test-case-macros-3
Version:        3.3.1
Release:        %autorelease
Summary:        Rust crate "test-case-macros"
License:        MIT
URL:            https://github.com/frondeus/test-case
#!RemoteAsset:  sha256:5c89e72a01ed4c579669add59014b9a524d609c0c88c6a585ce37485879f6ffb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/extra-traits) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Requires:       crate(syn-2/parsing) >= 2.0.0
Requires:       crate(test-case-core-3) >= 3.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "test-case-macros"

%package     -n %{name}+with-regex
Summary:        Provides #[test_case(...)] procedural macro attribute for generating parametrized test cases easily - feature "with-regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(test-case-core-3/with-regex) >= 3.2.1
Provides:       crate(%{pkgname}/with-regex) = %{version}

%description -n %{name}+with-regex
This metapackage enables feature "with-regex" for the Rust test-case-macros crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
