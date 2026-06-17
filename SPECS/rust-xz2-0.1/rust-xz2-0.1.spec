# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xz2
%global full_version 0.1.7
%global pkgname xz2-0.1

Name:           rust-xz2-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "xz2"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/xz2-rs
#!RemoteAsset:  sha256:388c44dc09d76f1536602ead6d325eb532f5c122f17782bd57fb47baeeb767e2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lzma-sys-0.1/default) >= 0.1.18
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "xz2"

%package     -n %{name}+futures
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-level in-memory encoding/decoding - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.1/default) >= 0.1.26
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust xz2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-level in-memory encoding/decoding - feature "static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lzma-sys-0.1/static) >= 0.1.18
Provides:       crate(%{pkgname}/static) = %{version}

%description -n %{name}+static
This metapackage enables feature "static" for the Rust xz2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-level in-memory encoding/decoding - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/tokio-io) = %{version}
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust xz2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-io
Summary:        Rust bindings to liblzma providing Read/Write streams as well as low-level in-memory encoding/decoding - feature "tokio-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-io-0.1/default) >= 0.1.12
Provides:       crate(%{pkgname}/tokio-io) = %{version}

%description -n %{name}+tokio-io
This metapackage enables feature "tokio-io" for the Rust xz2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
