# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name compiletest_rs
%global full_version 0.3.26
%global pkgname compiletest-rs-0.3

Name:           rust-compiletest-rs-0.3
Version:        0.3.26
Release:        %autorelease
Summary:        Rust crate "compiletest_rs"
License:        Apache-2.0 OR MIT
URL:            https://github.com/laumann/compiletest-rs
#!RemoteAsset:  sha256:d7d8975604ebad8b6660796802377eb6495045c5606168fc1b8d19a4dd9bfa46
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(diff-0.1/default) >= 0.1.10
Requires:       crate(filetime-0.2/default) >= 0.2.0
Requires:       crate(getopts-0.2/default) >= 0.2.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(miow-0.3/default) >= 0.3.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(rustfix-0.4/default) >= 0.4.1
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(tester-0.6/default) >= 0.6.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rustc) = %{version}
Provides:       crate(%{pkgname}/stable) = %{version}

%description
Source code for takopackized Rust crate "compiletest_rs"

%package     -n %{name}+tempfile
Summary:        Compiletest utility from the Rust compiler as a standalone testing harness - feature "tempfile" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/tempfile) = %{version}
Provides:       crate(%{pkgname}/tmp) = %{version}

%description -n %{name}+tempfile
This metapackage enables feature "tempfile" for the Rust compiletest_rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tmp" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
