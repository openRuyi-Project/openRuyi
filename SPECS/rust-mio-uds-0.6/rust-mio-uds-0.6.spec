# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mio-uds
%global full_version 0.6.8
%global pkgname mio-uds-0.6

Name:           rust-mio-uds-0.6
Version:        0.6.8
Release:        %autorelease
Summary:        Rust crate "mio-uds"
License:        MIT OR Apache-2.0
URL:            https://github.com/deprecrated/mio-uds
#!RemoteAsset:  sha256:afcb699eb26d4332647cc848492bbc15eafb26f08d0304550d5aa1f612e066f0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(iovec-0.1/default) >= 0.1.0
Requires:       crate(libc-0.2/default) >= 0.2.69
Requires:       crate(mio-0.6/default) >= 0.6.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mio-uds"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
