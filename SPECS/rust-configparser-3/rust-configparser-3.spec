# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name configparser
%global full_version 3.2.0
%global pkgname configparser-3

Name:           rust-configparser-3
Version:        3.2.0
Release:        %autorelease
Summary:        Rust crate "configparser"
License:        MIT OR LGPL-3.0-or-later
URL:            https://github.com/QEDK/configparser-rs
#!RemoteAsset:  sha256:b46dec724fd22199ebde05033a0cbae453bc3b1ecff11eb6a6bb3eec4b90c6a4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
You can use this to write Rust programs which can be customized by end users easily.
Source code for takopackized Rust crate "configparser"

%package     -n %{name}+indexmap
Summary:        Simple configuration parsing utility with no dependencies that allows you to parse INI and ini-style syntax - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.14.0
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
You can use this to write Rust programs which can be customized by end users easily.
This metapackage enables feature "indexmap" for the Rust configparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Simple configuration parsing utility with no dependencies that allows you to parse INI and ini-style syntax - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/serde) >= 2.14.0
Requires:       crate(serde-1/default) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
You can use this to write Rust programs which can be customized by end users easily.
This metapackage enables feature "serde" for the Rust configparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Simple configuration parsing utility with no dependencies that allows you to parse INI and ini-style syntax - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.52.3
Requires:       crate(tokio-1/fs) >= 1.52.3
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
You can use this to write Rust programs which can be customized by end users easily.
This metapackage enables feature "tokio" for the Rust configparser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
