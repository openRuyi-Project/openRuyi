# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dlv-list
%global full_version 0.5.2
%global pkgname dlv-list-0.5

Name:           rust-dlv-list-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "dlv-list"
License:        MIT OR Apache-2.0
URL:            https://github.com/sgodwincs/dlv-list-rs
#!RemoteAsset:  sha256:442039f5147480ba31067cb00ada1adae6892028e40e45fc5de7b7df6dcc1b5f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-random-0.1/default) >= 0.1.15

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "dlv-list"

%package     -n %{name}+serde
Summary:        Semi-doubly linked list implemented using a vector - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust dlv-list crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
