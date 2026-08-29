# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name event-listener
%global full_version 3.1.0
%global pkgname event-listener-3

Name:           rust-event-listener-3
Version:        3.1.0
Release:        %autorelease
Summary:        Rust crate "event-listener"
License:        Apache-2.0 OR MIT
URL:            https://github.com/smol-rs/event-listener
#!RemoteAsset:  sha256:d93877bcde0eb80ca09131a08d23f0a5c18a620b01db137dba666d18cd9b30c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(concurrent-queue-2) >= 2.2.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.12
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "event-listener"

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
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-util
Summary:        Notify async tasks or threads - feature "portable-atomic-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-util-0.1/alloc) >= 0.1.2
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
Requires:       crate(concurrent-queue-2/std) >= 2.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust event-listener crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
