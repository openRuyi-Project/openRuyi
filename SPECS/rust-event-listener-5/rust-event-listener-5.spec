# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name event-listener
%global full_version 5.4.1
%global pkgname event-listener-5

Name:           rust-event-listener-5
Version:        5.4.1
Release:        %autorelease
Summary:        Rust crate "event-listener"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/event-listener
#!RemoteAsset:  sha256:e13b66accf52311f30a0db42147dadea9850cb48cd070028831ae5f5d4b856ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(concurrent-queue-2) >= 2.4.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "event-listener"

%package     -n %{name}+critical-section
Summary:        Notify async tasks or threads - feature "critical-section"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(critical-section-1) >= 1.2.0
Provides:       crate(%{pkgname}/critical-section) = %{version}

%description -n %{name}+critical-section
This metapackage enables feature "critical-section" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+loom
Summary:        Notify async tasks or threads - feature "loom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(concurrent-queue-2/loom) >= 2.4.0
Requires:       crate(loom-0.7/default) >= 0.7.0
Requires:       crate(parking-2/loom) >= 2.0.0
Provides:       crate(%{pkgname}/loom) = %{version}

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parking
Summary:        Notify async tasks or threads - feature "parking"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/parking) = %{version}

%description -n %{name}+parking
This metapackage enables feature "parking" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Notify async tasks or threads - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/portable-atomic-crate) = %{version}
Requires:       crate(%{pkgname}/portable-atomic-util) = %{version}
Requires:       crate(concurrent-queue-2/portable-atomic) >= 2.4.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-util
Summary:        Notify async tasks or threads - feature "portable-atomic-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.0
Provides:       crate(%{pkgname}/portable-atomic-util) = %{version}

%description -n %{name}+portable-atomic-util
This metapackage enables feature "portable-atomic-util" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-crate
Summary:        Notify async tasks or threads - feature "portable_atomic_crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1) >= 1.2.0
Provides:       crate(%{pkgname}/portable-atomic-crate) = %{version}

%description -n %{name}+portable-atomic-crate
This metapackage enables feature "portable_atomic_crate" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Notify async tasks or threads - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/parking) = %{version}
Requires:       crate(concurrent-queue-2/std) >= 2.4.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
