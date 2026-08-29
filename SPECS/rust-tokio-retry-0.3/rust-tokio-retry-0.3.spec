# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-retry
%global full_version 0.3.2
%global pkgname tokio-retry-0.3

Name:           rust-tokio-retry-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "tokio-retry"
License:        MIT
URL:            https://github.com/djc/tokio-retry
#!RemoteAsset:  sha256:4a129d95275ebf4c493ec53bf0f8cd95f5ac161bc4f381700809a54f595d4470
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pin-project-lite-0.2/default) >= 0.2.16
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tokio-retry"

%package     -n %{name}+rand
Summary:        Extensible, asynchronous retry behaviours for futures/tokio - feature "rand" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.10/thread-rng) >= 0.10.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust tokio-retry crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
