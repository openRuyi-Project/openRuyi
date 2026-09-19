# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff-static
%global full_version 0.2.27
%global pkgname jiff-static-0.2

Name:           rust-jiff-static-0.2
Version:        0.2.27
Release:        %autorelease
Summary:        Rust crate "jiff-static"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff/tree/master/crates/jiff-static
#!RemoteAsset:  sha256:47b605b0c050d845fc355bb11eb3f9a8deddc218ea60c76e61aa1f2adfb2c96a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.93
Requires:       crate(quote-1/default) >= 1.0.38
Requires:       crate(syn-2/default) >= 2.0.98

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/perf-inline) = %{version}
Provides:       crate(%{pkgname}/tz-fat) = %{version}

%description
Source code for takopackized Rust crate "jiff-static"

%package     -n %{name}+tzdb
Summary:        Create static TimeZone values for Jiff (useful in core-only environments) - feature "tzdb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-tzdb-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/tzdb) = %{version}

%description -n %{name}+tzdb
This metapackage enables feature "tzdb" for the Rust jiff-static crate, by pulling in any additional dependencies needed by that feature.

%files
%license COPYING
%license LICENSE-MIT
%license UNLICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
