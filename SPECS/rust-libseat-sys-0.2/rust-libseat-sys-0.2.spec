# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libseat-sys
%global full_version 0.2.0
%global pkgname libseat-sys-0.2

Name:           rust-libseat-sys-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "libseat-sys"
License:        MIT
URL:            https://github.com/PolyMeilex/libseat-rs
#!RemoteAsset:  sha256:e8a484fa48be5f62a8d3ffed767779d0ab808cfead91de98ef4362d469097dfb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pkg-config-0.3) >= 0.3.19
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/docs-rs) = %{version}

%description
Source code for takopackized Rust crate "libseat-sys"

%package     -n %{name}+bindgen
Summary:        Libseat bindings - feature "bindgen" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.58/default) >= 0.58.1
Provides:       crate(%{pkgname}/bindgen) = %{version}
Provides:       crate(%{pkgname}/use-bindgen) = %{version}

%description -n %{name}+bindgen
This metapackage enables feature "bindgen" for the Rust libseat-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_bindgen" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
