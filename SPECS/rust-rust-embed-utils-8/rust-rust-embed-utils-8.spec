# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-embed-utils
%global full_version 8.8.0
%global pkgname rust-embed-utils-8

Name:           rust-rust-embed-utils-8
Version:        8.8.0
Release:        %autorelease
Summary:        Rust crate "rust-embed-utils"
License:        MIT
URL:            https://pyrossh.dev/repos/rust-embed
#!RemoteAsset:  sha256:21fcbee55c2458836bcdbfffb6ec9ba74bbc23ca7aa6816015a3dd2c4d8fc185
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sha2-0.10/default) >= 0.10.5
Requires:       crate(walkdir-2/default) >= 2.3.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug-embed) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rust-embed-utils"

%package     -n %{name}+globset
Summary:        Utilities for rust-embed - feature "globset" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(globset-0.4/default) >= 0.4.8
Provides:       crate(%{pkgname}/globset) = %{version}
Provides:       crate(%{pkgname}/include-exclude) = %{version}

%description -n %{name}+globset
This metapackage enables feature "globset" for the Rust rust-embed-utils crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "include-exclude" feature.

%package     -n %{name}+mime-guess
Summary:        Utilities for rust-embed - feature "mime_guess"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mime-guess-2/default) >= 2.0.4
Provides:       crate(%{pkgname}/mime-guess) = %{version}

%description -n %{name}+mime-guess
This metapackage enables feature "mime_guess" for the Rust rust-embed-utils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
