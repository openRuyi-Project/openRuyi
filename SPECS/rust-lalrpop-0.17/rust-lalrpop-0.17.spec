# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lalrpop
%global full_version 0.17.2
%global pkgname lalrpop-0.17

Name:           rust-lalrpop-0.17
Version:        0.17.2
Release:        %autorelease
Summary:        Rust crate "lalrpop"
License:        Apache-2.0 OR MIT
URL:            https://github.com/lalrpop/lalrpop
#!RemoteAsset:  sha256:64dc3698e75d452867d9bd86f4a723f452ce9d01fe1d55990b79f0c790aa67db
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ascii-canvas-2/default) >= 2.0.0
Requires:       crate(atty-0.2/default) >= 0.2.0
Requires:       crate(bit-set-0.5/default) >= 0.5.0
Requires:       crate(diff-0.1/default) >= 0.1.9
Requires:       crate(docopt-1/default) >= 1.0.0
Requires:       crate(ena-0.13/default) >= 0.13.0
Requires:       crate(itertools-0.8/default) >= 0.8.0
Requires:       crate(lalrpop-util-0.17/default) >= 0.17.2
Requires:       crate(petgraph-0.4/default) >= 0.4.13
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(regex-syntax-0.6/default) >= 0.6.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(sha2-0.8/default) >= 0.8.0
Requires:       crate(string-cache-0.7/default) >= 0.7.1
Requires:       crate(term-0.5/default) >= 0.5.0
Requires:       crate(unicode-xid-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description
Source code for takopackized Rust crate "lalrpop"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
