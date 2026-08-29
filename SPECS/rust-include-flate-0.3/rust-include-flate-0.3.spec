# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name include-flate
%global full_version 0.3.4
%global pkgname include-flate-0.3

Name:           rust-include-flate-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "include-flate"
License:        Apache-2.0
URL:            https://github.com/SOF3/include-flate
#!RemoteAsset:  sha256:48f173716febb1ad596c16ea5637b5f1790ea32de8e627493ff82bc73b0876ce
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(include-flate-codegen-0.3) >= 0.3.4
Requires:       crate(include-flate-compress-0.3) >= 0.3.4

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "include-flate"

%package     -n %{name}+default
Summary:        Variant of include_bytes!/include_str! with compile-time deflation and runtime lazy inflation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/deflate) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust include-flate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deflate
Summary:        Variant of include_bytes!/include_str! with compile-time deflation and runtime lazy inflation - feature "deflate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-codegen-0.3/deflate) >= 0.3.4
Requires:       crate(include-flate-compress-0.3/deflate) >= 0.3.4
Provides:       crate(%{pkgname}/deflate) = %{version}

%description -n %{name}+deflate
This metapackage enables feature "deflate" for the Rust include-flate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-compression-warnings
Summary:        Variant of include_bytes!/include_str! with compile-time deflation and runtime lazy inflation - feature "no-compression-warnings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-codegen-0.3/no-compression-warnings) >= 0.3.4
Provides:       crate(%{pkgname}/no-compression-warnings) = %{version}

%description -n %{name}+no-compression-warnings
This metapackage enables feature "no-compression-warnings" for the Rust include-flate crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Variant of include_bytes!/include_str! with compile-time deflation and runtime lazy inflation - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-codegen-0.3/zstd) >= 0.3.4
Requires:       crate(include-flate-compress-0.3/zstd) >= 0.3.4
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust include-flate crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
