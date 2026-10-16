# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_jitter
%global full_version 0.1.4
%global pkgname rand-jitter-0.1

Name:           rust-rand-jitter-0.1
Version:        0.1.4
Release:        %autorelease
Summary:        Rust crate "rand_jitter"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-random/rand
#!RemoteAsset:  sha256:1166d5c91dc97b88d1decc3285bb0a99ed84b05cfd0bc2341bdf2d43fc41e39b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.0
Requires:       crate(rand-core-0.4/default) >= 0.4.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/profileapi) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_jitter"

%package     -n %{name}+log
Summary:        Random number generator based on timing jitter - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rand_jitter crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Random number generator based on timing jitter - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand_jitter crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
