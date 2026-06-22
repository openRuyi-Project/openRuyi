# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xkbcommon-dl
%global full_version 0.4.2
%global pkgname xkbcommon-dl-0.4

Name:           rust-xkbcommon-dl-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "xkbcommon-dl"
License:        MIT
URL:            https://github.com/rust-windowing/xkbcommon-dl
#!RemoteAsset:  sha256:d039de8032a9a8856a6be89cea3e5d12fdd82306ab7c94d74e6deab2460651c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.3.1
Requires:       crate(dlib-0.5/default) >= 0.5.2
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(once-cell-1/default) >= 1.17.0
Requires:       crate(xkeysym-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/x11) = %{version}

%description
Source code for takopackized Rust crate "xkbcommon-dl"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
