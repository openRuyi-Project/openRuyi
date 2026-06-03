# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-crate
%global full_version 3.3.0
%global pkgname proc-macro-crate-3.0

Name:           rust-proc-macro-crate-3.0
Version:        3.3.0
Release:        %autorelease
Summary:        Rust crate "proc-macro-crate"
License:        MIT OR Apache-2.0
URL:            https://github.com/bkchr/proc-macro-crate
#!RemoteAsset:  sha256:edce586971a4dfaa28950c6f18ed55e0406c1ab88bbce2c6f6293a7aaba73d35
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(toml-edit-0.22/parse) >= 0.22.27
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "proc-macro-crate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
