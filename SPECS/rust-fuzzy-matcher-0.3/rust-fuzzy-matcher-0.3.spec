# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fuzzy-matcher
%global full_version 0.3.7
%global pkgname fuzzy-matcher-0.3

Name:           rust-fuzzy-matcher-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "fuzzy-matcher"
License:        MIT
URL:            https://github.com/lotabout/fuzzy-matcher
#!RemoteAsset:  sha256:54614a3312934d066701a80f20f15fa3b56d67ac7722b39eea5b4c9dd1d66c94
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(thread-local-1/default) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compact) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fuzzy-matcher"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
