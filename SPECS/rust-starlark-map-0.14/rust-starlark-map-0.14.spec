# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name starlark_map
%global full_version 0.14.2
%global pkgname starlark-map-0.14

Name:           rust-starlark-map-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "starlark_map"
License:        Apache-2.0
URL:            https://github.com/facebook/starlark-rust
#!RemoteAsset:  sha256:234877898fd216af93b2f5798b08cbbdc1a2e8f16a622a258b1db23a61a1c4ba
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(allocative-0.3/default) >= 0.3.6
Requires:       crate(allocative-0.3/hashbrown) >= 0.3.6
Requires:       crate(dupe-0.9/default) >= 0.9.1
Requires:       crate(equivalent-1/default) >= 1.0.2
Requires:       crate(fxhash-0.2/default) >= 0.2.1
Requires:       crate(hashbrown-0.16/default) >= 0.16.1
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(strong-hash-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "starlark_map"

%package     -n %{name}+pagable-dep
Summary:        Map implementation with starlark-rust specific optimizations - feature "pagable_dep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pagable-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/pagable-dep) = %{version}

%description -n %{name}+pagable-dep
This metapackage enables feature "pagable_dep" for the Rust starlark_map crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
