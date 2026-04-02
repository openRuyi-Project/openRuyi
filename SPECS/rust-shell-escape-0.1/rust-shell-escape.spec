# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name shell-escape
%global full_version 0.1.5
%global pkgname shell-escape-0.1

Name:           rust-shell-escape-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "shell-escape"
License:        MIT/Apache-2.0
URL:            https://github.com/sfackler/shell-escape
#!RemoteAsset:  sha256:45bb67a18fa91266cc7807181f62f9178a6873bfad7dc788c42e6430db40184f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "shell-escape"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
