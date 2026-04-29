# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff-static
%global full_version 0.2.23
%global pkgname jiff-static-0.2

Name:           rust-jiff-static-0.2
Version:        0.2.23
Release:        %autorelease
Summary:        Rust crate "jiff-static"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff/tree/master/crates/jiff-static
#!RemoteAsset:  sha256:2a8c8b344124222efd714b73bb41f8b5120b27a7cc1c75593a6ff768d9d05aa4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/perf-inline)
Provides:       crate(%{pkgname}/tz-fat)

%description
Source code for takopackized Rust crate "jiff-static"

%package     -n %{name}+tzdb
Summary:        Create static TimeZone values for Jiff (useful in core-only environments) - feature "tzdb"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-tzdb-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/tzdb)

%description -n %{name}+tzdb
This metapackage enables feature "tzdb" for the Rust jiff-static crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
