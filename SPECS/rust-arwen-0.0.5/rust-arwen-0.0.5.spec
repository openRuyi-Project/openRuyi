# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arwen
%global full_version 0.0.5
%global pkgname arwen-0.0.5

Name:           rust-arwen-0.0.5
Version:        0.0.5
Release:        %autorelease
Summary:        Rust crate "arwen"
License:        MIT
URL:            https://github.com/nichmor/arwen
#!RemoteAsset:  sha256:d44cbd9bd79165abe331ebabb9dd4d59a5dc93791be33ff15ebd71baaadc85ba
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/default) >= 4.5.26
Requires:       crate(clap-4/derive) >= 4.5.26
Requires:       crate(goblin-0.10/default) >= 0.10.4
Requires:       crate(goblin-0.10/mach64) >= 0.10.4
Requires:       crate(object-0.38/build) >= 0.38.1
Requires:       crate(object-0.38/default) >= 0.38.1
Requires:       crate(object-0.38/write) >= 0.38.1
Requires:       crate(scroll-0.13/default) >= 0.13.0
Requires:       crate(thiserror-2/default) >= 2.0.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arwen"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
