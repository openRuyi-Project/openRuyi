# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name parking_lot_core
%global full_version 0.9.12
%global pkgname parking-lot-core-0.9

Name:           rust-parking-lot-core-0.9
Version:        0.9.12
Release:        %autorelease
Summary:        Rust crate "parking_lot_core"
License:        MIT OR Apache-2.0
URL:            https://github.com/Amanieu/parking_lot
#!RemoteAsset:  sha256:2621685985a2ebf1c516881c026032ac7deafcda1a2c9b7850dc81e3dfcb64c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(libc-0.2/default) >= 0.2.183
Requires:       crate(redox-syscall-0.5/default) >= 0.5.18
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(windows-link-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
Source code for takopackized Rust crate "parking_lot_core"

%package     -n %{name}+backtrace
Summary:        Advanced API for creating custom synchronization primitives - feature "backtrace"
Requires:       crate(%{pkgname})
Requires:       crate(backtrace-0.3/default) >= 0.3.60
Provides:       crate(%{pkgname}/backtrace)

%description -n %{name}+backtrace
This metapackage enables feature "backtrace" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deadlock-detection
Summary:        Advanced API for creating custom synchronization primitives - feature "deadlock_detection"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/backtrace)
Requires:       crate(%{pkgname}/petgraph)
Provides:       crate(%{pkgname}/deadlock-detection)

%description -n %{name}+deadlock-detection
This metapackage enables feature "deadlock_detection" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+petgraph
Summary:        Advanced API for creating custom synchronization primitives - feature "petgraph"
Requires:       crate(%{pkgname})
Requires:       crate(petgraph-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/petgraph)

%description -n %{name}+petgraph
This metapackage enables feature "petgraph" for the Rust parking_lot_core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
