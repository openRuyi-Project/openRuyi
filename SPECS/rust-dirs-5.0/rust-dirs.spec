# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dirs
%global full_version 5.0.1
%global pkgname dirs-5.0

Name:           rust-dirs-5.0
Version:        5.0.1
Release:        %autorelease
Summary:        Rust crate "dirs"
License:        MIT OR Apache-2.0
URL:            https://github.com/soc/dirs-rs
#!RemoteAsset:  sha256:44c45a9d03d6676652bcb5e724c7e988de1acad23a711b5217ab9cbecbec2225
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-sys-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "dirs"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
