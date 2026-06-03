# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name borrow-or-share
%global full_version 0.2.2
%global pkgname borrow-or-share-0.2

Name:           rust-borrow-or-share-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "borrow-or-share"
License:        MIT-0
URL:            https://github.com/yescallop/borrow-or-share
#!RemoteAsset:  sha256:3eeab4423108c5d7c744f4d234de88d18d636100093ae04caf4825134b9c3a32
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "borrow-or-share"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
