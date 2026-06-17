# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name heck
%global full_version 0.4.1
%global pkgname heck-0.4

Name:           rust-heck-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "heck"
License:        MIT OR Apache-2.0
URL:            https://github.com/withoutboats/heck
#!RemoteAsset:  sha256:95505c38b4572b2d910cecb0281560f54b440a19336cbbcb27bf6ce6adc6f5a8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "heck"

%package     -n %{name}+unicode-segmentation
Summary:        Case conversion library - feature "unicode-segmentation" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-segmentation-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/unicode) = %{version}
Provides:       crate(%{pkgname}/unicode-segmentation) = %{version}

%description -n %{name}+unicode-segmentation
This metapackage enables feature "unicode-segmentation" for the Rust heck crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unicode" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
