# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap-num
%global full_version 1.2.0
%global pkgname clap-num-1

Name:           rust-clap-num-1
Version:        1.2.0
Release:        %autorelease
Summary:        Rust crate "clap-num"
License:        MIT
URL:            https://github.com/newAM/clap-num/
#!RemoteAsset:  sha256:822c4000301ac390e65995c62207501e3ef800a1fc441df913a5e8e4dc374816
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}

%description
Number parsers for clap.
Source code for takopackized Rust crate "clap-num"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
