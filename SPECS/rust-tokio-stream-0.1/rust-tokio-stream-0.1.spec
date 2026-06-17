# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-stream
%global full_version 0.1.18
%global pkgname tokio-stream-0.1

Name:           rust-tokio-stream-0.1
Version:        0.1.18
Release:        %autorelease
Summary:        Rust crate "tokio-stream"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:32da49809aab5c3bc678af03902d4ccddea2a87d028d86392a4b1560c6906c70
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3/default) >= 0.3.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.11
Requires:       crate(tokio-1/default) >= 1.15.0
Requires:       crate(tokio-1/sync) >= 1.15.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tokio-stream"

%package     -n %{name}+fs
Summary:        Utilities to work with `Stream` and `tokio` - feature "fs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/fs) >= 1.15.0
Requires:       crate(tokio-1/sync) >= 1.15.0
Provides:       crate(%{pkgname}/fs) = %{version}

%description -n %{name}+fs
This metapackage enables feature "fs" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Utilities to work with `Stream` and `tokio` - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/fs) = %{version}
Requires:       crate(%{pkgname}/io-util) = %{version}
Requires:       crate(%{pkgname}/net) = %{version}
Requires:       crate(%{pkgname}/signal) = %{version}
Requires:       crate(%{pkgname}/sync) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-util
Summary:        Utilities to work with `Stream` and `tokio` - feature "io-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.15.0
Requires:       crate(tokio-1/sync) >= 1.15.0
Provides:       crate(%{pkgname}/io-util) = %{version}

%description -n %{name}+io-util
This metapackage enables feature "io-util" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+net
Summary:        Utilities to work with `Stream` and `tokio` - feature "net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/net) >= 1.15.0
Requires:       crate(tokio-1/sync) >= 1.15.0
Provides:       crate(%{pkgname}/net) = %{version}

%description -n %{name}+net
This metapackage enables feature "net" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signal
Summary:        Utilities to work with `Stream` and `tokio` - feature "signal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/signal) >= 1.15.0
Requires:       crate(tokio-1/sync) >= 1.15.0
Provides:       crate(%{pkgname}/signal) = %{version}

%description -n %{name}+signal
This metapackage enables feature "signal" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sync
Summary:        Utilities to work with `Stream` and `tokio` - feature "sync"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Requires:       crate(tokio-1/sync) >= 1.15.0
Provides:       crate(%{pkgname}/sync) = %{version}

%description -n %{name}+sync
This metapackage enables feature "sync" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Utilities to work with `Stream` and `tokio` - feature "time" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/sync) >= 1.15.0
Requires:       crate(tokio-1/time) >= 1.15.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio-util
Summary:        Utilities to work with `Stream` and `tokio` - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust tokio-stream crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
