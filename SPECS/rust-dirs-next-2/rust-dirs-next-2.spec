# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs-next
%global full_version 2.0.0
%global pkgname dirs-next-2

Name:           rust-dirs-next-2
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "dirs-next"
License:        MIT OR Apache-2.0
URL:            https://github.com/xdg-rs/dirs
#!RemoteAsset:  sha256:b98cf8ebf19c3d1b223e151f99a4f9f0690dca41414773390fc824184ac833e1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(dirs-sys-next-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "dirs-next"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
