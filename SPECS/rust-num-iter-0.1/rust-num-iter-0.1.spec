# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-iter
%global full_version 0.1.45
%global pkgname num-iter-0.1

Name:           rust-num-iter-0.1
Version:        0.1.45
Release:        %autorelease
Summary:        Rust crate "num-iter"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-iter
#!RemoteAsset:  sha256:1429034a0490724d0075ebb2bc9e875d6503c3cf69e235a8941aa757d83ef5bf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(autocfg-1) >= 1.0.0
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/i128) = %{version}

%description
Source code for takopackized Rust crate "num-iter"

%package     -n %{name}+std
Summary:        External iterators for generic mathematics - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-integer-0.1/i128) >= 0.1.46
Requires:       crate(num-integer-0.1/std) >= 0.1.46
Requires:       crate(num-traits-0.2/i128) >= 0.2.11
Requires:       crate(num-traits-0.2/std) >= 0.2.11
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-iter crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
