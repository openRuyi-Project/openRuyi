# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mailparse
%global full_version 0.16.1
%global pkgname mailparse-0.16

Name:           rust-mailparse-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "mailparse"
License:        0BSD
URL:            https://github.com/staktrace/mailparse/blob/master/README.md
#!RemoteAsset:  sha256:60819a97ddcb831a5614eb3b0174f3620e793e97e09195a395bfa948fd68ed2f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(charset-0.1/default) >= 0.1.3
Requires:       crate(data-encoding-2/default) >= 2.6.0
Requires:       crate(quoted-printable-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mailparse"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
