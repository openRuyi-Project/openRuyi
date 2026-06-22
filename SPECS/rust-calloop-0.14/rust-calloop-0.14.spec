# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name calloop
%global full_version 0.14.4
%global pkgname calloop-0.14

Name:           rust-calloop-0.14
Version:        0.14.4
Release:        %autorelease
Summary:        Rust crate "calloop"
License:        MIT
URL:            https://github.com/Smithay/calloop
#!RemoteAsset:  sha256:4dbf9978365bac10f54d1d4b04f7ce4427e51f71d61f2fe15e3fed5166474df7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(polling-3/default) >= 3.0.0
Requires:       crate(rustix-1/event) >= 1.0.0
Requires:       crate(rustix-1/fs) >= 1.0.0
Requires:       crate(rustix-1/pipe) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Requires:       crate(slab-0.4/default) >= 0.4.8
Requires:       crate(tracing-0.1/log) >= 0.1.40
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly-coverage) = %{version}

%description
Source code for takopackized Rust crate "calloop"

%package     -n %{name}+async-task
Summary:        Callback-based event loop - feature "async-task" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-task-4/default) >= 4.4.0
Provides:       crate(%{pkgname}/async-task) = %{version}
Provides:       crate(%{pkgname}/executor) = %{version}

%description -n %{name}+async-task
This metapackage enables feature "async-task" for the Rust calloop crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "executor" feature.

%package     -n %{name}+futures-core
Summary:        Callback-based event loop - feature "futures-core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.31
Provides:       crate(%{pkgname}/futures-core) = %{version}
Provides:       crate(%{pkgname}/stream) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust calloop crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "stream" feature.

%package     -n %{name}+futures-io
Summary:        Callback-based event loop - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.5
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust calloop crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nix
Summary:        Callback-based event loop - feature "nix" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nix-0.31/signal) >= 0.31.0
Provides:       crate(%{pkgname}/nix) = %{version}
Provides:       crate(%{pkgname}/signals) = %{version}

%description -n %{name}+nix
This metapackage enables feature "nix" for the Rust calloop crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "signals" feature.

%package     -n %{name}+pin-utils
Summary:        Callback-based event loop - feature "pin-utils" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-utils-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/block-on) = %{version}
Provides:       crate(%{pkgname}/pin-utils) = %{version}

%description -n %{name}+pin-utils
This metapackage enables feature "pin-utils" for the Rust calloop crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "block_on" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
