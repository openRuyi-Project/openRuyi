# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bugreport
%global full_version 0.5.1
%global pkgname bugreport-0.5

Name:           rust-bugreport-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "bugreport"
License:        MIT OR Apache-2.0
URL:            https://github.com/sharkdp/bugreport
#!RemoteAsset:  sha256:f280f65ce85b880919349bbfcb204930291251eedcb2e5f84ce2f51df969c162
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(shell-escape-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/format-markdown) = %{version}
Provides:       crate(%{pkgname}/format-plaintext) = %{version}

%description
Source code for takopackized Rust crate "bugreport"

%package     -n %{name}+collector-operating-system
Summary:        Collect system and environment information for bug reports - feature "collector_operating_system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sysinfo-0.33/default) >= 0.33.1
Provides:       crate(%{pkgname}/collector-operating-system) = %{version}

%description -n %{name}+collector-operating-system
This metapackage enables feature "collector_operating_system" for the Rust bugreport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Collect system and environment information for bug reports - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/collector-operating-system) = %{version}
Requires:       crate(%{pkgname}/format-markdown) = %{version}
Requires:       crate(%{pkgname}/git-hash) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bugreport crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+git-version
Summary:        Collect system and environment information for bug reports - feature "git-version" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(git-version-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/git-hash) = %{version}
Provides:       crate(%{pkgname}/git-version) = %{version}

%description -n %{name}+git-version
This metapackage enables feature "git-version" for the Rust bugreport crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "git_hash" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
