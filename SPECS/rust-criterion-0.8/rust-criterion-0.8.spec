# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name criterion
%global full_version 0.8.2
%global pkgname criterion-0.8

Name:           rust-criterion-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "criterion"
License:        Apache-2.0 OR MIT
URL:            https://criterion-rs.github.io/book/index.html
#!RemoteAsset:  sha256:950046b2aa2492f9a536f5f4f9a3de7b9e2476e575e05bd6c333371add4d98f3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anes-0.1/default) >= 0.1.4
Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(ciborium-0.2/default) >= 0.2.0
Requires:       crate(clap-4/std) >= 4.5.0
Requires:       crate(criterion-plot-0.8/default) >= 0.8.2
Requires:       crate(itertools-0.13/default) >= 0.13.0
Requires:       crate(num-traits-0.2/std) >= 0.2.0
Requires:       crate(oorandom-11/default) >= 11.1.0
Requires:       crate(page-size-0.6/default) >= 0.6.0
Requires:       crate(regex-1/std) >= 1.5.1
Requires:       crate(serde-1/default) >= 1.0.100
Requires:       crate(serde-1/derive) >= 1.0.100
Requires:       crate(serde-json-1/default) >= 1.0.100
Requires:       crate(tinytemplate-1/default) >= 1.1.0
Requires:       crate(walkdir-2/default) >= 2.3.0
Requires:       crate(alloca-0.4) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Statistics-driven micro-benchmarking library.
Source code for takopackized Rust crate "criterion"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
