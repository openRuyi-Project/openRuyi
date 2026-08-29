# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xkeysym
%global full_version 0.2.1
%global pkgname xkeysym-0.2

Name:           rust-xkeysym-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "xkeysym"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/notgull/xkeysym
#!RemoteAsset:  sha256:b9cc00251562a284751c9973bace760d86c0276c471b4be569fe6b068ee97a56
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "xkeysym"

%package     -n %{name}+bytemuck
Summary:        Working with X11 keysyms - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/derive) >= 1.12.3
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust xkeysym crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Working with X11 keysyms - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.160
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust xkeysym crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
