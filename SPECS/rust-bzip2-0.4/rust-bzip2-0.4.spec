# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bzip2
%global full_version 0.4.4
%global pkgname bzip2-0.4

Name:           rust-bzip2-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "bzip2"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/bzip2-rs
#!RemoteAsset:  sha256:bdb116a6ef3f6c3698828873ad02c3014b3c85cadb88496095628e3ef1e347f8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bzip2-sys-0.1/default) >= 0.1.11
Requires:       crate(libc-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "bzip2"

%package     -n %{name}+futures
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-sys-0.1/static) >= 0.1.11
Provides:       crate(%{pkgname}/static) = %{version}

%description -n %{name}+static
This metapackage enables feature "static" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/tokio-io) = %{version}
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-io
Summary:        Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams - feature "tokio-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-io-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tokio-io) = %{version}

%description -n %{name}+tokio-io
This metapackage enables feature "tokio-io" for the Rust bzip2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
