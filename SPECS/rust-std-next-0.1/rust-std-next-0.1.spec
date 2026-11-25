# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name std-next
%global full_version 0.1.9
%global pkgname std-next-0.1

Name:           rust-std-next-0.1
Version:        0.1.9
Release:        %autorelease
Summary:        Rust crate "std-next"
License:        MIT
URL:            https://github.com/Nugine/std-next
#!RemoteAsset:  sha256:04082e93ed1a06debd9148c928234b46d2cf260bc65f44e1d1d3fa594c5beebc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(simdutf8-0.1) >= 0.1.5
Requires:       crate(thiserror-2/default) >= 2.0.12

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}

%description
Source code for takopackized Rust crate "std-next"

%package     -n %{name}+std
Summary:        Opinionated utilities and polyfills - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(simdutf8-0.1/std) >= 0.1.5
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust std-next crate, by
pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
