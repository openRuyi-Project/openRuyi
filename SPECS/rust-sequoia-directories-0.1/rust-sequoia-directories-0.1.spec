# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-directories
%global full_version 0.1.0
%global pkgname sequoia-directories-0.1

Name:           rust-sequoia-directories-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "sequoia-directories"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:b01dd48960c5cf8617ab77e5c9f8ebeb55a1d694e3eabf830fa70453ffa637d5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(directories-5/default) >= 5.0.0
Requires:       crate(same-file-1/default) >= 1.0.0
Requires:       crate(tempfile-3/default) >= 3.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-directories"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
