# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winsafe
%global full_version 0.0.19
%global pkgname winsafe-0.0.19

Name:           rust-winsafe-0.0.19
Version:        0.0.19
Release:        %autorelease
Summary:        Rust crate "winsafe"
License:        MIT
URL:            https://github.com/rodrigocfd/winsafe
#!RemoteAsset:  sha256:d135d17ab770252ad95e9a872d365cf3090e3be864a34ab46f48555993efc904
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/comctl) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dshow) = %{version}
Provides:       crate(%{pkgname}/dxgi) = %{version}
Provides:       crate(%{pkgname}/gdi) = %{version}
Provides:       crate(%{pkgname}/kernel) = %{version}
Provides:       crate(%{pkgname}/mf) = %{version}
Provides:       crate(%{pkgname}/ole) = %{version}
Provides:       crate(%{pkgname}/oleaut) = %{version}
Provides:       crate(%{pkgname}/shell) = %{version}
Provides:       crate(%{pkgname}/taskschd) = %{version}
Provides:       crate(%{pkgname}/user) = %{version}
Provides:       crate(%{pkgname}/version) = %{version}

%description
Source code for takopackized Rust crate "winsafe"

%package     -n %{name}+gui
Summary:        Windows API and GUI in safe, idiomatic Rust - feature "gui"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/comctl) = %{version}
Requires:       crate(%{pkgname}/shell) = %{version}
Requires:       crate(%{pkgname}/uxtheme) = %{version}
Provides:       crate(%{pkgname}/gui) = %{version}

%description -n %{name}+gui
This metapackage enables feature "gui" for the Rust winsafe crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uxtheme
Summary:        Windows API and GUI in safe, idiomatic Rust - feature "uxtheme" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gdi) = %{version}
Requires:       crate(%{pkgname}/ole) = %{version}
Provides:       crate(%{pkgname}/dwm) = %{version}
Provides:       crate(%{pkgname}/uxtheme) = %{version}

%description -n %{name}+uxtheme
This metapackage enables feature "uxtheme" for the Rust winsafe crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dwm" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
