# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-properties
%global full_version 0.1.4
%global pkgname unicode-properties-0.1

Name:           rust-unicode-properties-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "unicode-properties"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-properties
#!RemoteAsset:  sha256:7df058c713841ad818f1dc5d3fd88063241cc61f49f5fbea4b951e8cf5a8d71d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/emoji) = %{version}
Provides:       crate(%{pkgname}/general-category) = %{version}

%description
Source code for takopackized Rust crate "unicode-properties"

%package     -n %{name}+default
Summary:        Query character Unicode properties according to UAX #44 and UTR #51 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/emoji) = %{version}
Requires:       crate(%{pkgname}/general-category) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust unicode-properties crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
