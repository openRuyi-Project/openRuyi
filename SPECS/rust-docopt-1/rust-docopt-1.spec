# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name docopt
%global full_version 1.1.1
%global pkgname docopt-1

Name:           rust-docopt-1
Version:        1.1.1
Release:        %autorelease
Summary:        Rust crate "docopt"
License:        Unlicense OR MIT
URL:            https://github.com/docopt/docopt.rs
#!RemoteAsset:  sha256:7f3f119846c823f9eafcf953a8f6ffb6ed69bf6240883261a7f13b634579a51f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lazy-static-1/default) >= 1.3.0
Requires:       crate(regex-1/std) >= 1.4.0
Requires:       crate(regex-1/unicode) >= 1.4.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(strsim-0.10/default) >= 0.10.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "docopt"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
