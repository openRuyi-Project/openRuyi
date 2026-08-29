# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zbus-lockstep
%global full_version 0.5.2
%global pkgname zbus-lockstep-0.5

Name:           rust-zbus-lockstep-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "zbus-lockstep"
License:        MIT
URL:            https://github.com/luukvanderduim/zbus-lockstep
#!RemoteAsset:  sha256:6998de05217a084b7578728a9443d04ea4cd80f2a0839b8d78770b76ccd45863
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zbus-xml-5/default) >= 5.0.2
Requires:       crate(zvariant-5/default) >= 5.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zbus-lockstep"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
