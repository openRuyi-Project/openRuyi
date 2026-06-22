# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name countio
%global full_version 0.3.0
%global pkgname countio-0.3

Name:           rust-countio-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "countio"
License:        MIT
URL:            https://github.com/spire-rs/countio
#!RemoteAsset:  sha256:b9702aee5d1d744c01d82f6915644f950f898e014903385464c773b96fefdecb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "countio"

%package     -n %{name}+full
Summary:        Byte counting for std::io::{Read, Write, Seek} and its async variants from futures and tokio - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust countio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Byte counting for std::io::{Read, Write, Seek} and its async variants from futures and tokio - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/std) >= 0.3.0
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust countio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Byte counting for std::io::{Read, Write, Seek} and its async variants from futures and tokio - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust countio crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
