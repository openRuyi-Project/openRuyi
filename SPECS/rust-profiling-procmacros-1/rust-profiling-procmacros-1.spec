# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name profiling-procmacros
%global full_version 1.0.18
%global pkgname profiling-procmacros-1

Name:           rust-profiling-procmacros-1
Version:        1.0.18
Release:        %autorelease
Summary:        Rust crate "profiling-procmacros"
License:        MIT OR Apache-2.0
URL:            https://github.com/aclysma/profiling
#!RemoteAsset:  sha256:4488a4a36b9a4ba6b9334a32a39971f77c1436ec82c38707bce707699cc3bbcb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/profile-with-optick) = %{version}
Provides:       crate(%{pkgname}/profile-with-puffin) = %{version}
Provides:       crate(%{pkgname}/profile-with-superluminal) = %{version}
Provides:       crate(%{pkgname}/profile-with-tracing) = %{version}
Provides:       crate(%{pkgname}/profile-with-tracy) = %{version}

%description
Source code for takopackized Rust crate "profiling-procmacros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
