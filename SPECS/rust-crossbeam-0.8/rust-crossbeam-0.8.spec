# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crossbeam
%global full_version 0.8.5
%global pkgname crossbeam-0.8

Name:           rust-crossbeam-0.8
Version:        0.8.5
Release:        %autorelease
Summary:        Rust crate "crossbeam"
License:        MIT OR Apache-2.0
URL:            https://github.com/crossbeam-rs/crossbeam
#!RemoteAsset:  sha256:e71406cd8807725f7ac2f999a4cdd32e98f829fdf65f528343cebf945e41df1e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-utils-0.8) >= 0.8.18

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "crossbeam"

%package     -n %{name}+alloc
Summary:        Tools for concurrent programming - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-epoch-0.9/alloc) >= 0.9.17
Requires:       crate(crossbeam-queue-0.3/alloc) >= 0.3.10
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust crossbeam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-channel
Summary:        Tools for concurrent programming - feature "crossbeam-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-channel-0.5) >= 0.5.10
Provides:       crate(%{pkgname}/crossbeam-channel) = %{version}

%description -n %{name}+crossbeam-channel
This metapackage enables feature "crossbeam-channel" for the Rust crossbeam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-deque
Summary:        Tools for concurrent programming - feature "crossbeam-deque"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-deque-0.8) >= 0.8.4
Provides:       crate(%{pkgname}/crossbeam-deque) = %{version}

%description -n %{name}+crossbeam-deque
This metapackage enables feature "crossbeam-deque" for the Rust crossbeam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-epoch
Summary:        Tools for concurrent programming - feature "crossbeam-epoch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-epoch-0.9) >= 0.9.17
Provides:       crate(%{pkgname}/crossbeam-epoch) = %{version}

%description -n %{name}+crossbeam-epoch
This metapackage enables feature "crossbeam-epoch" for the Rust crossbeam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-queue
Summary:        Tools for concurrent programming - feature "crossbeam-queue"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-queue-0.3) >= 0.3.10
Provides:       crate(%{pkgname}/crossbeam-queue) = %{version}

%description -n %{name}+crossbeam-queue
This metapackage enables feature "crossbeam-queue" for the Rust crossbeam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nightly
Summary:        Tools for concurrent programming - feature "nightly"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-epoch-0.9/nightly) >= 0.9.17
Requires:       crate(crossbeam-queue-0.3/nightly) >= 0.3.10
Requires:       crate(crossbeam-utils-0.8/nightly) >= 0.8.18
Provides:       crate(%{pkgname}/nightly) = %{version}

%description -n %{name}+nightly
This metapackage enables feature "nightly" for the Rust crossbeam crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Tools for concurrent programming - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(crossbeam-channel-0.5/std) >= 0.5.10
Requires:       crate(crossbeam-deque-0.8/std) >= 0.8.4
Requires:       crate(crossbeam-epoch-0.9/std) >= 0.9.17
Requires:       crate(crossbeam-queue-0.3/std) >= 0.3.10
Requires:       crate(crossbeam-utils-0.8/std) >= 0.8.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust crossbeam crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
