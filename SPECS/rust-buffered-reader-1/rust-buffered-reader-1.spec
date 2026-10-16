# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name buffered-reader
%global full_version 1.4.1
%global pkgname buffered-reader-1

Name:           rust-buffered-reader-1
Version:        1.4.1
Release:        %autorelease
Summary:        Rust crate "buffered-reader"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:c7531a07caf83a3fa3b47a233b437ee7910cccfb688555d224338295a0a64fcc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.66

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "buffered-reader"

%package     -n %{name}+bzip2
Summary:        Super-powered Reader - feature "bzip2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bzip2-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/bzip2) = %{version}
Provides:       crate(%{pkgname}/compression-bzip2) = %{version}

%description -n %{name}+bzip2
This metapackage enables feature "bzip2" for the Rust buffered-reader crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compression-bzip2" feature.

%package     -n %{name}+compression
Summary:        Super-powered Reader - feature "compression" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compression-bzip2) = %{version}
Requires:       crate(%{pkgname}/compression-deflate) = %{version}
Provides:       crate(%{pkgname}/compression) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+compression
This metapackage enables feature "compression" for the Rust buffered-reader crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+flate2
Summary:        Super-powered Reader - feature "flate2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/compression-deflate) = %{version}
Provides:       crate(%{pkgname}/flate2) = %{version}

%description -n %{name}+flate2
This metapackage enables feature "flate2" for the Rust buffered-reader crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "compression-deflate" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
