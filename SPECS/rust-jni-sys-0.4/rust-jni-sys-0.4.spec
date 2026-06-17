# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jni-sys
%global full_version 0.4.1
%global pkgname jni-sys-0.4

Name:           rust-jni-sys-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "jni-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/jni-rs/jni-sys
#!RemoteAsset:  sha256:c6377a88cb3910bee9b0fa88d4f42e1d2da8e79915598f65fb0c7ee14c878af2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(jni-sys-macros-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "jni-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
