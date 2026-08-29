# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name comfy-table
%global full_version 7.2.1
%global pkgname comfy-table-7

Name:           rust-comfy-table-7
Version:        7.2.1
Release:        %autorelease
Summary:        Rust crate "comfy-table"
License:        MIT
URL:            https://github.com/nukesor/comfy-table
#!RemoteAsset:  sha256:b03b7db8e0b4b2fdad6c551e634134e99ec000e5c8c3b6856c65e8bbaded7a3b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-segmentation-1/default) >= 1.0.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/integration-test) = %{version}

%description
Source code for takopackized Rust crate "comfy-table"

%package     -n %{name}+custom-styling
Summary:        Easy to use library for building beautiful tables with automatic content wrapping - feature "custom_styling"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tty) = %{version}
Requires:       crate(ansi-str-0.9/default) >= 0.9.0
Requires:       crate(console-0.16/default) >= 0.16.0
Provides:       crate(%{pkgname}/custom-styling) = %{version}

%description -n %{name}+custom-styling
This metapackage enables feature "custom_styling" for the Rust comfy-table crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tty
Summary:        Easy to use library for building beautiful tables with automatic content wrapping - feature "tty" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossterm-0.29) >= 0.29.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/reexport-crossterm) = %{version}
Provides:       crate(%{pkgname}/tty) = %{version}

%description -n %{name}+tty
This metapackage enables feature "tty" for the Rust comfy-table crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "reexport_crossterm" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
