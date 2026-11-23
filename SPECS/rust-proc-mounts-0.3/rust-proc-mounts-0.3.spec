# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-mounts
%global full_version 0.3.0
%global pkgname proc-mounts-0.3

Name:           rust-proc-mounts-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "proc-mounts"
License:        MIT
URL:            https://github.com/pop-os/proc-mounts
#!RemoteAsset:  sha256:0d652f8435d0ab70bf4f3590a6a851d59604831a458086541b95238cc51ffcf2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(partition-identity-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-mounts"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
