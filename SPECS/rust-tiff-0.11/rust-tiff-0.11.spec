# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tiff
%global full_version 0.11.3
%global pkgname tiff-0.11

Name:           rust-tiff-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "tiff"
License:        MIT
URL:            https://github.com/image-rs/image-tiff
#!RemoteAsset:  sha256:b63feaf3343d35b6ca4d50483f94843803b0f51634937cc2ec519fc32232bc52
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(half-2/default) >= 2.4.1
Requires:       crate(quick-error-2/default) >= 2.0.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tiff"

%package     -n %{name}+default
Summary:        TIFF decoding and encoding library in pure Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/fax) = %{version}
Requires:       crate(%{pkgname}/jpeg) = %{version}
Requires:       crate(%{pkgname}/lzw) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        TIFF decoding and encoding library in pure Rust - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(flate2-1/default) >= 1.0.20
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust tiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fax
Summary:        TIFF decoding and encoding library in pure Rust - feature "fax"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fax-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname}/fax) = %{version}

%description -n %{name}+fax
This metapackage enables feature "fax" for the Rust tiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jpeg
Summary:        TIFF decoding and encoding library in pure Rust - feature "jpeg"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zune-jpeg-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}/jpeg) = %{version}

%description -n %{name}+jpeg
This metapackage enables feature "jpeg" for the Rust tiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lzw
Summary:        TIFF decoding and encoding library in pure Rust - feature "lzw"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(weezl-0.1/default) >= 0.1.10
Provides:       crate(%{pkgname}/lzw) = %{version}

%description -n %{name}+lzw
This metapackage enables feature "lzw" for the Rust tiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webp
Summary:        TIFF decoding and encoding library in pure Rust - feature "webp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(image-webp-0.2/default) >= 0.2.4
Provides:       crate(%{pkgname}/webp) = %{version}

%description -n %{name}+webp
This metapackage enables feature "webp" for the Rust tiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        TIFF decoding and encoding library in pure Rust - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust tiff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
