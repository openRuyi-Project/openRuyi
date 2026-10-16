# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name line-col
%global full_version 0.2.1
%global pkgname line-col-0.2

Name:           rust-line-col-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "line-col"
License:        MIT
URL:            https://github.com/TheBerkin/line-col-rs
#!RemoteAsset:  sha256:9e69cdf6b85b5c8dce514f694089a2cf8b1a702f6cd28607bcb3cf296c9778db
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "line-col"

%package     -n %{name}+unicode-segmentation
Summary:        Convert string slice indices into line/column numbers - feature "unicode-segmentation" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-segmentation-1/default) >= 1.6.0
Provides:       crate(%{pkgname}/grapheme-clusters) = %{version}
Provides:       crate(%{pkgname}/unicode-segmentation) = %{version}

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust line-col crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "grapheme-clusters" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
