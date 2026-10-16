# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name skim
%global full_version 0.10.4
%global pkgname skim-0.10

Name:           rust-skim-0.10
Version:        0.10.4
Release:        %autorelease
Summary:        Rust crate "skim"
License:        MIT
URL:            https://github.com/lotabout/skim
#!RemoteAsset:  sha256:e5d28de0a6cb2cdd83a076f1de9d965b973ae08b244df1aa70b432946dda0f32
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(beef-0.5/default) >= 0.5.2
Requires:       crate(bitflags-1/default) >= 1.3.2
Requires:       crate(chrono-0.4/default) >= 0.4.22
Requires:       crate(crossbeam-0.8/default) >= 0.8.2
Requires:       crate(defer-drop-1/default) >= 1.3.0
Requires:       crate(derive-builder-0.11/default) >= 0.11.2
Requires:       crate(fuzzy-matcher-0.3/default) >= 0.3.7
Requires:       crate(lazy-static-1/default) >= 1.4.0
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(nix-0.25/default) >= 0.25.0
Requires:       crate(rayon-1/default) >= 1.5.3
Requires:       crate(regex-1/default) >= 1.6.0
Requires:       crate(time-0.3/default) >= 0.3.13
Requires:       crate(timer-0.2/default) >= 0.2.0
Requires:       crate(tuikit-0.5/default) >= 0.5.0
Requires:       crate(unicode-width-0.1/default) >= 0.1.9
Requires:       crate(vte-0.11/default) >= 0.11.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "skim"

%package     -n %{name}+cli
Summary:        Fuzzy Finder in rust! - feature "cli" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atty-0.2/default) >= 0.2.14
Requires:       crate(clap-3/cargo) >= 3.2.22
Requires:       crate(clap-3/default) >= 3.2.22
Requires:       crate(env-logger-0.9/default) >= 0.9.0
Requires:       crate(shlex-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/cli) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust skim crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
