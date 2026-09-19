# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name test-case
%global full_version 3.3.1
%global pkgname test-case-3

Name:           rust-test-case-3
Version:        3.3.1
Release:        %autorelease
Summary:        Rust crate "test-case"
License:        MIT
URL:            https://github.com/frondeus/test-case
#!RemoteAsset:  sha256:eb2550dd13afcd286853192af8601920d959b14c401fcece38071d53bf0768a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(test-case-macros-3) >= 3.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "test-case"

%package     -n %{name}+regex
Summary:        Provides #[test_case(...)] procedural macro attribute for generating parametrized test cases easily - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.5.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust test-case crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-regex
Summary:        Provides #[test_case(...)] procedural macro attribute for generating parametrized test cases easily - feature "with-regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(test-case-macros-3/with-regex) >= 3.2.1
Provides:       crate(%{pkgname}/with-regex) = %{version}

%description -n %{name}+with-regex
This metapackage enables feature "with-regex" for the Rust test-case crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
