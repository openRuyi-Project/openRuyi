# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name assert_cmd
%global full_version 2.2.2
%global pkgname assert-cmd-2

Name:           rust-assert-cmd-2
Version:        2.2.2
Release:        %autorelease
Summary:        Rust crate "assert_cmd"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/assert_cmd
#!RemoteAsset:  sha256:2aa3a22042e45de04255c7bf3626e239f450200fd0493c1e382263544b20aea6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anstyle-1/default) >= 1.0.0
Requires:       crate(bstr-1/default) >= 1.0.1
Requires:       crate(libc-0.2/default) >= 0.2.137
Requires:       crate(predicates-3/diff) >= 3.0.1
Requires:       crate(predicates-core-1/default) >= 1.0.6
Requires:       crate(predicates-tree-1/default) >= 1.0.1
Requires:       crate(wait-timeout-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "assert_cmd"

%package     -n %{name}+color
Summary:        Test CLI Applications - feature "color" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(anstream-1/default) >= 1.0.0
Requires:       crate(predicates-3/color) >= 3.0.1
Requires:       crate(predicates-3/diff) >= 3.0.1
Provides:       crate(%{pkgname}/color) = %{version}
Provides:       crate(%{pkgname}/color-auto) = %{version}

%description -n %{name}+color
This metapackage enables feature "color" for the Rust assert_cmd crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color-auto" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
