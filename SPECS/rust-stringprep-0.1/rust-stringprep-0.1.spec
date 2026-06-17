# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name stringprep
%global full_version 0.1.5
%global pkgname stringprep-0.1

Name:           rust-stringprep-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "stringprep"
License:        MIT OR Apache-2.0
URL:            https://github.com/sfackler/rust-stringprep
#!RemoteAsset:  sha256:7b4df3d392d81bd458a8a621b8bffbd2302a12ffe288a9d931670948749463b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unicode-bidi-0.3/default) >= 0.3.0
Requires:       crate(unicode-normalization-0.1/default) >= 0.1.0
Requires:       crate(unicode-properties-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "stringprep"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
