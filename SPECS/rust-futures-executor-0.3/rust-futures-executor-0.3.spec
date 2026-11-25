# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-executor
%global full_version 0.3.33
%global pkgname futures-executor-0.3

Name:           rust-futures-executor-0.3
Version:        0.3.33
Release:        %autorelease
Summary:        Rust crate "futures-executor"
License:        MIT OR Apache-2.0
URL:            https://rust-lang.github.io/futures-rs
#!RemoteAsset:  sha256:6754879cc9f2c66f88c6e5c35344bb0bdb0708b0352b1201815667c7eabc7458
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.33
Requires:       crate(futures-task-0.3) >= 0.3.33
Requires:       crate(futures-util-0.3) >= 0.3.33

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "futures-executor"

%package     -n %{name}+std
Summary:        Executors for asynchronous tasks based on the futures-rs library - feature "std" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/std) >= 0.3.33
Requires:       crate(futures-task-0.3/std) >= 0.3.33
Requires:       crate(futures-util-0.3/std) >= 0.3.33
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/thread-pool) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-executor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "thread-pool" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
