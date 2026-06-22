# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name owo-colors
%global full_version 4.3.0
%global pkgname owo-colors-4

Name:           rust-owo-colors-4
Version:        4.3.0
Release:        %autorelease
Summary:        Rust crate "owo-colors"
License:        MIT
URL:            https://github.com/owo-colors/owo-colors
#!RemoteAsset:  sha256:d211803b9b6b570f68772237e415a029d5a50c65d382910b879fb19d3271f94d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "owo-colors"

%package     -n %{name}+supports-color
Summary:        Zero-allocation terminal colors that'll make people go owo - feature "supports-color"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(supports-color-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/supports-color) = %{version}

%description -n %{name}+supports-color
This metapackage enables feature "supports-color" for the Rust owo-colors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+supports-colors
Summary:        Zero-allocation terminal colors that'll make people go owo - feature "supports-colors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/supports-color) = %{version}
Requires:       crate(supports-color-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/supports-colors) = %{version}

%description -n %{name}+supports-colors
This metapackage enables feature "supports-colors" for the Rust owo-colors crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
