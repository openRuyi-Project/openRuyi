# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wyz
%global full_version 0.5.1
%global pkgname wyz-0.5

Name:           rust-wyz-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "wyz"
License:        MIT
URL:            https://myrrlyn.net/crates/wyz
#!RemoteAsset:  sha256:05f360fc0b24296329c78fda852a1e9ae82de9cf7b27dae4b7f62f118f77b9ed
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tap-1.0/default) >= 1.0.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "wyz"

%package     -n %{name}+garbage
Summary:        Myrrlyn’s utility collection - feature "garbage"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/once-cell)
Requires:       crate(%{pkgname}/typemap)
Provides:       crate(%{pkgname}/garbage)

%description -n %{name}+garbage
This metapackage enables feature "garbage" for the Rust wyz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Myrrlyn’s utility collection - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust wyz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+typemap
Summary:        Myrrlyn’s utility collection - feature "typemap"
Requires:       crate(%{pkgname})
Requires:       crate(typemap-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/typemap)

%description -n %{name}+typemap
This metapackage enables feature "typemap" for the Rust wyz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
