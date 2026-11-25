# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name annotate-snippets
%global full_version 0.9.2
%global pkgname annotate-snippets-0.9

Name:           rust-annotate-snippets-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "annotate-snippets"
License:        Apache-2.0 OR MIT
URL:            https://github.com/rust-lang/annotate-snippets-rs
#!RemoteAsset:  sha256:ccaf7e9dfbb6ab22c82e473cd1a8a7bd313c19a5b7e40970f3d89ef5a5c9e81e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-width-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "annotate-snippets"

%package     -n %{name}+yansi-term
Summary:        Building code annotations - feature "yansi-term" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(yansi-term-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/color) = %{version}
Provides:       crate(%{pkgname}/yansi-term) = %{version}

%description -n %{name}+yansi-term
This metapackage enables feature "yansi-term" for the Rust annotate-snippets crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "color" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
