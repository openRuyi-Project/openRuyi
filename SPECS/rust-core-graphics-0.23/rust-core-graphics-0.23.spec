# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name core-graphics
%global full_version 0.23.2
%global pkgname core-graphics-0.23

Name:           rust-core-graphics-0.23
Version:        0.23.2
Release:        %autorelease
Summary:        Rust crate "core-graphics"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/core-foundation-rs
#!RemoteAsset:  sha256:c07782be35f9e1140080c6b96f0d44b739e2278479f64e02fdab4e32dfd8b081
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(core-foundation-0.9) >= 0.9.0
Requires:       crate(core-graphics-types-0.1) >= 0.1.0
Requires:       crate(foreign-types-0.5/default) >= 0.5.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/elcapitan) = %{version}
Provides:       crate(%{pkgname}/highsierra) = %{version}

%description
Source code for takopackized Rust crate "core-graphics"

%package     -n %{name}+link
Summary:        Bindings to Core Graphics for macOS - feature "link" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-foundation-0.9/link) >= 0.9.0
Requires:       crate(core-graphics-types-0.1/link) >= 0.1.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/link) = %{version}

%description -n %{name}+link
This metapackage enables feature "link" for the Rust core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
