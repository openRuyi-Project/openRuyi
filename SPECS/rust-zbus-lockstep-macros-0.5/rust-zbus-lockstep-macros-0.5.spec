# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zbus-lockstep-macros
%global full_version 0.5.2
%global pkgname zbus-lockstep-macros-0.5

Name:           rust-zbus-lockstep-macros-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "zbus-lockstep-macros"
License:        MIT
URL:            https://github.com/luukvanderduim/zbus-lockstep
#!RemoteAsset:  sha256:10da05367f3a7b7553c8cdf8fa91aee6b64afebe32b51c95177957efc47ca3a0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(zbus-lockstep-0.5/default) >= 0.5.2
Requires:       crate(zbus-xml-5/default) >= 5.0.2
Requires:       crate(zvariant-5/default) >= 5.1.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "zbus-lockstep-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
