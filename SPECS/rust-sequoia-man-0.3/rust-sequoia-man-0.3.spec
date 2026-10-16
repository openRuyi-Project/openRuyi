# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-man
%global full_version 0.3.2
%global pkgname sequoia-man-0.3

Name:           rust-sequoia-man-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "sequoia-man"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:961fa9711d7a1d9ccc13ac55b65482f828399dda12a0be7fa4e059dca410d217
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(clap-4/default) >= 4.0.0
Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(clap-4/env) >= 4.0.0
Requires:       crate(roff-0.2/default) >= 0.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-man"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
