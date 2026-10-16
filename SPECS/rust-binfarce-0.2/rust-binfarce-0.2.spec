# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name binfarce
%global full_version 0.2.2
%global pkgname binfarce-0.2

Name:           rust-binfarce-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "binfarce"
License:        MIT
URL:            https://github.com/Shnatsel/binfarce
#!RemoteAsset:  sha256:8c3909adc0a877afb5f851ce4344d43ea0382240cfad4f760109b7aa603685e0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "binfarce"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
