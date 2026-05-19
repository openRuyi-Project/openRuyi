# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quote-use
%global full_version 0.8.4
%global pkgname quote-use-0.8

Name:           rust-quote-use-0.8
Version:        0.8.4
Release:        %autorelease
Summary:        Rust crate "quote-use"
License:        MIT
URL:            https://github.com/ModProg/quote-use
#!RemoteAsset:  sha256:9619db1197b497a36178cfc736dc96b271fe918875fbf1344c436a7e93d0321e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(quote-use-macros-0.8/default) >= 0.8.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "quote-use"

%package     -n %{name}+syn
Summary:        Support `use` in procmacros hygienically - feature "syn"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/parsing) >= 2.0.0
Requires:       crate(syn-2.0/printing) >= 2.0.0
Provides:       crate(%{pkgname}/syn)

%description -n %{name}+syn
This metapackage enables feature "syn" for the Rust quote-use crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
