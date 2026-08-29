# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc-sys
%global full_version 0.3.5
%global pkgname objc-sys-0.3

Name:           rust-objc-sys-0.3
Version:        0.3.5
Release:        %autorelease
Summary:        Rust crate "objc-sys"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:cdb91bdd390c7ce1a8607f35f3ca7151b65afc0ff5ff3b34fa350f7d7c7e4310
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/apple) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-c-unwind) = %{version}
Provides:       crate(%{pkgname}/unstable-objfw) = %{version}
Provides:       crate(%{pkgname}/unstable-winobjc) = %{version}

%description
Source code for takopackized Rust crate "objc-sys"

%package     -n %{name}+cc
Summary:        Raw bindings to the Objective-C runtime and ABI - feature "cc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.0.80
Provides:       crate(%{pkgname}/cc) = %{version}
Provides:       crate(%{pkgname}/unstable-exception) = %{version}

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust objc-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-exception" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
