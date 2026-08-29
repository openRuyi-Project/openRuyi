# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name git-testament-derive
%global full_version 0.2.1
%global pkgname git-testament-derive-0.2

Name:           rust-git-testament-derive-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "git-testament-derive"
License:        BSD-3-Clause
URL:            https://github.com/kinnison/git-testament/
#!RemoteAsset:  sha256:bbeac967e71eb3dc1656742fc7521ec7cd3b6b88738face65bf1fddf702bc4c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(time-0.3/default) >= 0.3.0
Requires:       crate(time-0.3/formatting) >= 0.3.0
Requires:       crate(time-0.3/macros) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "git-testament-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
