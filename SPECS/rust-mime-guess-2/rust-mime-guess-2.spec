# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mime_guess
%global full_version 2.0.5
%global pkgname mime-guess-2

Name:           rust-mime-guess-2
Version:        2.0.5
Release:        %autorelease
Summary:        Rust crate "mime_guess"
License:        MIT
URL:            https://github.com/abonander/mime_guess
#!RemoteAsset:  sha256:f7c44f8e672c00fe5308fa235f821cb4198414e1c77935c1ab6948d3fd78550e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(mime-0.3/default) >= 0.3.0
Requires:       crate(unicase-2) >= 2.4.0
Requires:       crate(unicase-2/default) >= 2.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rev-mappings) = %{version}

%description
Source code for takopackized Rust crate "mime_guess"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
