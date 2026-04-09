# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name either
%global full_version 1.0.3
%global pkgname either-1.0

Name:           rust-either-1.0
Version:        1.0.3
Release:        %autorelease
Summary:        Rust crate "either"
License:        MIT/Apache-2.0
URL:            https://github.com/bluss/either
#!RemoteAsset:  sha256:63f94a35a9ca0d4178e85f0250373f2cea55c5d603e6993778d68a99b3d8071c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/use-std)

%description
Either has methods that are similar to Option and Result.
Includes convenience macros `try_left!()` and `try_right!()` to use for short-circuiting logic.
Source code for takopackized Rust crate "either"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
