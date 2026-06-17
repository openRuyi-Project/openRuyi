# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spm_precompiled
%global full_version 0.1.4
%global pkgname spm-precompiled-0.1

Name:           rust-spm-precompiled-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "spm_precompiled"
License:        Apache-2.0
URL:            https://github.com/huggingface/spm_precompiled
#!RemoteAsset:  sha256:5851699c4033c63636f7ea4cf7b7c1f1bf06d0cc03cfb42e711de5a5c46cf326
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.13/default) >= 0.13.0
Requires:       crate(nom-7/default) >= 7.1.1
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(unicode-segmentation-1/default) >= 1.9.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
This crate is highly specialized and not intended for general use.
Source code for takopackized Rust crate "spm_precompiled"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
