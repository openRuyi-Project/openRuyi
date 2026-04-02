# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name opener
%global full_version 0.8.4
%global pkgname opener-0.8

Name:           rust-opener-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "opener"
License:        MIT OR Apache-2.0
URL:            https://github.com/Seeker14491/opener
#!RemoteAsset:  sha256:a2fa337e0cf13357c13ef1dc108df1333eb192f75fc170bea03fcf1fd404c2ee
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/default) >= 1.12.1
Requires:       crate(normpath-1.0/default) >= 1.5.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-ui-shell) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-ui-windowsandmessaging) >= 0.61.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "opener"

%package     -n %{name}+reveal
Summary:        Open a file or link using the system default program - feature "reveal"
Requires:       crate(%{pkgname})
Requires:       crate(url-2.0/default) >= 2.0.0
Requires:       crate(windows-sys-0.61/win32-system-com) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-ui-shell) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-ui-shell-common) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-ui-windowsandmessaging) >= 0.61.2
Requires:       crate(zbus-5.0/default) >= 5.0.0
Requires:       crate(zbus-5.0/url) >= 5.0.0
Provides:       crate(%{pkgname}/reveal)

%description -n %{name}+reveal
This metapackage enables feature "reveal" for the Rust opener crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
