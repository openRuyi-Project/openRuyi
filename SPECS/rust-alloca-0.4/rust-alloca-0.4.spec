# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name alloca
%global full_version 0.4.0
%global pkgname alloca-0.4

Name:           rust-alloca-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "alloca"
License:        MIT
URL:            https://github.com/playXE/alloca-rs
#!RemoteAsset:  sha256:e5a7d05ea6aea7e9e64d25b9156ba2fee3fdd659e34e41063cd2fc7cd020d7f4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Mostly safe wrapper for alloca.
Source code for takopackized Rust crate "alloca"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
