# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quoted_printable
%global full_version 0.5.2
%global pkgname quoted-printable-0.5

Name:           rust-quoted-printable-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "quoted_printable"
License:        0BSD
URL:            https://github.com/staktrace/quoted-printable/blob/master/README.md
#!RemoteAsset:  sha256:478e0585659a122aa407eb7e3c0e1fa51b1d8a870038bd29f0cf4a8551eea972
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "quoted_printable"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
