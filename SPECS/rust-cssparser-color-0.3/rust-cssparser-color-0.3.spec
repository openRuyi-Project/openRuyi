# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cssparser-color
%global full_version 0.3.0
%global pkgname cssparser-color-0.3

Name:           rust-cssparser-color-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "cssparser-color"
License:        MPL-2.0
URL:            https://github.com/servo/rust-cssparser
#!RemoteAsset:  sha256:6eeef9ae8c0e112edd89eb6406b3156ffa99c7e037b3baef1dbdf4158d35c324
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cssparser-0.35/default) >= 0.35.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cssparser-color"

%package     -n %{name}+serde
Summary:        Color implementation based on cssparser - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cssparser-0.35/serde) >= 0.35.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust cssparser-color crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
