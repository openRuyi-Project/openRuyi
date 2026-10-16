# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name moka
%global full_version 0.12.16
%global pkgname moka-0.12

Name:           rust-moka-0.12
Version:        0.12.16
Release:        %autorelease
Summary:        Rust crate "moka"
License:        (MIT OR Apache-2.0) AND Apache-2.0
URL:            https://github.com/moka-rs/moka
#!RemoteAsset:  sha256:4293f18e7567a1caf3c584855554377025c65e0aa445344d04171f5ad63d19b9
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.15
Requires:       crate(crossbeam-epoch-0.9/default) >= 0.9.20
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.21
Requires:       crate(equivalent-1/default) >= 1.0.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(portable-atomic-1/default) >= 1.6.0
Requires:       crate(smallvec-1/default) >= 1.8.0
Requires:       crate(tagptr-0.2/default) >= 0.2.0
Requires:       crate(uuid-1/default) >= 1.1.0
Requires:       crate(uuid-1/v4) >= 1.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/atomic64) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/sync) = %{version}

%description
Source code for takopackized Rust crate "moka"

%package     -n %{name}+future
Summary:        Fast and concurrent cache library inspired by Java Caffeine - feature "future" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-lock-3/default) >= 3.3.0
Requires:       crate(event-listener-5/default) >= 5.3.0
Requires:       crate(futures-util-0.3/default) >= 0.3.17
Provides:       crate(%{pkgname}/future) = %{version}
Provides:       crate(%{pkgname}/unstable-debug-counters) = %{version}

%description -n %{name}+future
This metapackage enables feature "future" for the Rust moka crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-debug-counters" feature.

%package     -n %{name}+logging
Summary:        Fast and concurrent cache library inspired by Java Caffeine - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust moka crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quanta
Summary:        Fast and concurrent cache library inspired by Java Caffeine - feature "quanta"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quanta-0.12/default) >= 0.12.2
Provides:       crate(%{pkgname}/quanta) = %{version}

%description -n %{name}+quanta
This metapackage enables feature "quanta" for the Rust moka crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
