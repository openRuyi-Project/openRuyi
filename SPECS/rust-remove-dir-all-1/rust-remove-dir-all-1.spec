# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name remove_dir_all
%global full_version 1.0.0
%global pkgname remove-dir-all-1

Name:           rust-remove-dir-all-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "remove_dir_all"
License:        MIT OR Apache-2.0
URL:            https://github.com/XAMPPRocky/remove_dir_all.git
#!RemoteAsset:  sha256:808cc0b475acf76adf36f08ca49429b12aad9f678cb56143d5b3cb49b9a1dd08
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cvt-0.1/default) >= 0.1.1
Requires:       crate(fs-at-0.2/default) >= 0.2.1
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(normpath-1/default) >= 1.0.1
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-storage-filesystem) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-threading) >= 0.59.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "remove_dir_all"

%package     -n %{name}+cli
Summary:        Safe, reliable implementation of remove_dir_all for Windows - feature "cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/parallel) = %{version}
Requires:       crate(clap-4/default) >= 4.1.11
Requires:       crate(clap-4/derive) >= 4.1.11
Requires:       crate(env-logger-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust remove_dir_all crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Safe, reliable implementation of remove_dir_all for Windows - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.11
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust remove_dir_all crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Safe, reliable implementation of remove_dir_all for Windows - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust remove_dir_all crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
