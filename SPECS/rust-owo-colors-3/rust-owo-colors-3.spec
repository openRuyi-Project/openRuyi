# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name owo-colors
%global full_version 3.0.1
%global pkgname owo-colors-3

Name:           rust-owo-colors-3
Version:        3.0.1
Release:        %autorelease
Summary:        Rust crate "owo-colors"
License:        MIT
URL:            https://github.com/jam1garner/owo-colors
#!RemoteAsset:  sha256:503a1a6634186cefb8adc93a751df98215c52b8db8bf416b496865f04ec09e13
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "owo-colors"

%package     -n %{name}+supports-color
Summary:        Zero-allocation terminal colors that'll make people go owo - feature "supports-color" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(supports-color-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/supports-color) = %{version}
Provides:       crate(%{pkgname}/supports-colors) = %{version}

%description -n %{name}+supports-color
This metapackage enables feature "supports-color" for the Rust owo-colors crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "supports-colors" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
