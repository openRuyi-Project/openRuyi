# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-truncate
%global full_version 2.0.1
%global pkgname unicode-truncate-2

Name:           rust-unicode-truncate-2
Version:        2.0.1
Release:        %autorelease
Summary:        Rust crate "unicode-truncate"
License:        MIT OR Apache-2.0
URL:            https://github.com/Aetf/unicode-truncate
#!RemoteAsset:  sha256:16b380a1238663e5f8a691f9039c73e1cdae598a30e9855f541d29b08b53e9a5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itertools-0.14) >= 0.14.0
Requires:       crate(unicode-segmentation-1) >= 1.0.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "unicode-truncate"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
