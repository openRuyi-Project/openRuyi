# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-wot
%global full_version 0.14.0
%global pkgname sequoia-wot-0.14

Name:           rust-sequoia-wot-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "sequoia-wot"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:7725fa3249ea6f786362408e7fc9ebd86e9250633991d97a2bd64d1197dce490
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(chrono-0.4/default) >= 0.4.0
Requires:       crate(crossbeam-0.8/default) >= 0.8.1
Requires:       crate(num-cpus-1/default) >= 1.0.0
Requires:       crate(sequoia-cert-store-0.7) >= 0.7.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-wot"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
