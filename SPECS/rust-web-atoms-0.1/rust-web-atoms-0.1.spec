# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name web_atoms
%global full_version 0.1.3
%global pkgname web-atoms-0.1

Name:           rust-web-atoms-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "web_atoms"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/html5ever
#!RemoteAsset:  sha256:57ffde1dc01240bdf9992e3205668b235e59421fd085e8a317ed98da0178d414
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-0.11/default) >= 0.11.0
Requires:       crate(phf-codegen-0.11) >= 0.11.0
Requires:       crate(string-cache-0.8/default) >= 0.8.8
Requires:       crate(string-cache-codegen-0.5) >= 0.5.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "web_atoms"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
