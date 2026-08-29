# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name send_wrapper
%global full_version 0.6.0
%global pkgname send-wrapper-0.6

Name:           rust-send-wrapper-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "send_wrapper"
License:        MIT OR Apache-2.0
URL:            https://github.com/thk1/send_wrapper
#!RemoteAsset:  sha256:cd0b0ec5f1c1ca621c432a25813d8d60c88abe6d3e08a3eb9cf37d97a0fe3d73
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
You also have to make sure that the wrapper is dropped from within the original thread. If any of these constraints is violated, a panic occurs.
Source code for takopackized Rust crate "send_wrapper"

%package     -n %{name}+futures-core
Summary:        This Rust library implements a wrapper type called SendWrapper which allows you to move around non-Send types between threads, as long as you access the contained value only from within the original thread - feature "futures-core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures) = %{version}
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
You also have to make sure that the wrapper is dropped from within the original thread. If any of these constraints is violated, a panic occurs.
This metapackage enables feature "futures-core" for the Rust send_wrapper crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "futures" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
