# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name trybuild
%global full_version 1.0.116
%global pkgname trybuild-1

Name:           rust-trybuild-1
Version:        1.0.116
Release:        %autorelease
Summary:        Rust crate "trybuild"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/trybuild
#!RemoteAsset:  sha256:47c635f0191bd3a2941013e5062667100969f8c4e9cd787c14f977265d73616e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(glob-0.3/default) >= 0.3.0
Requires:       crate(serde-1/default) >= 1.0.194
Requires:       crate(serde-derive-1/default) >= 1.0.194
Requires:       crate(serde-json-1/default) >= 1.0.110
Requires:       crate(target-triple-1/default) >= 1.0.0
Requires:       crate(termcolor-1/default) >= 1.0.4
Requires:       crate(toml-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "trybuild"

%package     -n %{name}+diff
Summary:        Test harness for ui tests of compiler diagnostics - feature "diff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dissimilar-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/diff) = %{version}

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust trybuild crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
