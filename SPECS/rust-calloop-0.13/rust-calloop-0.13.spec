# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name calloop
%global full_version 0.13.0
%global pkgname calloop-0.13

Name:           rust-calloop-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "calloop"
License:        MIT
URL:            https://github.com/Smithay/calloop
#!RemoteAsset:  sha256:b99da2f8558ca23c71f4fd15dc57c906239752dd27ff3c00a1d56b685b7cbfec
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.4.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(polling-3/default) >= 3.0.0
Requires:       crate(rustix-0.38/event) >= 0.38.0
Requires:       crate(rustix-0.38/fs) >= 0.38.0
Requires:       crate(rustix-0.38/pipe) >= 0.38.0
Requires:       crate(rustix-0.38/std) >= 0.38.0
Requires:       crate(slab-0.4/default) >= 0.4.8
Requires:       crate(thiserror-1/default) >= 1.0.7
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
Requires:       crate(nix-0.28/signal) >= 0.28.0
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
