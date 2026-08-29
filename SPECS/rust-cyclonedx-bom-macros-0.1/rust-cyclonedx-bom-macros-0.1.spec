# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cyclonedx-bom-macros
%global full_version 0.1.0
%global pkgname cyclonedx-bom-macros-0.1

Name:           rust-cyclonedx-bom-macros-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "cyclonedx-bom-macros"
License:        Apache-2.0
URL:            https://cyclonedx.org/
#!RemoteAsset:  sha256:c50341f21df64b412b4f917e34b7aa786c092d64f3f905f478cb76950c7e980c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.78
Requires:       crate(quote-1/default) >= 1.0.35
Requires:       crate(syn-2/default) >= 2.0.48
Requires:       crate(syn-2/fold) >= 2.0.48
Requires:       crate(syn-2/full) >= 2.0.48
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "cyclonedx-bom-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
