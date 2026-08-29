# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derivre
%global full_version 0.3.11
%global pkgname derivre-0.3

Name:           rust-derivre-0.3
Version:        0.3.11
Release:        %autorelease
Summary:        Rust crate "derivre"
License:        MIT
URL:            https://github.com/microsoft/derivre
#!RemoteAsset:  sha256:dd3bf7087923a80510e6ea986960cb4011bcf54259ecb19a80bf40a645a1526c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.95
Requires:       crate(bytemuck-1/default) >= 1.21.0
Requires:       crate(bytemuck-derive-1/default) >= 1.8.1
Requires:       crate(hashbrown-0.15) >= 0.15.2
Requires:       crate(regex-syntax-0.8/default) >= 0.8.5
Requires:       crate(strum-0.27/default) >= 0.27.0
Requires:       crate(strum-0.27/derive) >= 0.27.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compress) = %{version}

%description
Source code for takopackized Rust crate "derivre"

%package     -n %{name}+ahash
Summary:        Derivative-based regular expression engine - feature "ahash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.8/default) >= 0.8.11
Provides:       crate(%{pkgname}/ahash) = %{version}

%description -n %{name}+ahash
This metapackage enables feature "ahash" for the Rust derivre crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Derivative-based regular expression engine - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ahash) = %{version}
Requires:       crate(%{pkgname}/compress) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust derivre crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
