# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name terminfo
%global full_version 0.9.0
%global pkgname terminfo-0.9

Name:           rust-terminfo-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "terminfo"
License:        WTFPL
URL:            https://github.com/meh/rust-terminfo
#!RemoteAsset:  sha256:d4ea810f0692f9f51b382fff5893887bb4580f5fa246fde546e0b13e7fcee662
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fnv-1/default) >= 1.0.0
Requires:       crate(nom-7/std) >= 7.0.0
Requires:       crate(phf-0.11/default) >= 0.11.0
Requires:       crate(phf-codegen-0.11) >= 0.11.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "terminfo"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
