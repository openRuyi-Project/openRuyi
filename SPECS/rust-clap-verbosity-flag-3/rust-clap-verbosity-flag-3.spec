# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap-verbosity-flag
%global full_version 3.0.4
%global pkgname clap-verbosity-flag-3

Name:           rust-clap-verbosity-flag-3
Version:        3.0.4
Release:        %autorelease
Summary:        Rust crate "clap-verbosity-flag"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap-verbosity-flag
#!RemoteAsset:  sha256:9d92b1fab272fe943881b77cc6e920d6543e5b1bfadbd5ed81c7c5a755742394
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4/derive) >= 4.0.0
Requires:       crate(clap-4/std) >= 4.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "clap-verbosity-flag"

%package     -n %{name}+log
Summary:        Easily add a `--verbose` flag to CLIs using Clap - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust clap-verbosity-flag crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+serde
Summary:        Easily add a `--verbose` flag to CLIs using Clap - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust clap-verbosity-flag crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Easily add a `--verbose` flag to CLIs using Clap - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-core-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust clap-verbosity-flag crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
