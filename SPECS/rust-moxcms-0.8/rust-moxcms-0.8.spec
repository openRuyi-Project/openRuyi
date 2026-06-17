# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name moxcms
%global full_version 0.8.1
%global pkgname moxcms-0.8

Name:           rust-moxcms-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "moxcms"
License:        BSD-3-Clause OR Apache-2.0
URL:            https://github.com/awxkee/moxcms
#!RemoteAsset:  sha256:bb85c154ba489f01b25c0d36ae69a87e4a1c73a72631fc6c0eb6dde34a73e44b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(pxfm-0.1/default) >= 0.1.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/any-to-any) = %{version}
Provides:       crate(%{pkgname}/avx) = %{version}
Provides:       crate(%{pkgname}/avx-shaper-fixed-point-paths) = %{version}
Provides:       crate(%{pkgname}/avx-shaper-optimized-paths) = %{version}
Provides:       crate(%{pkgname}/avx-shaper-paths) = %{version}
Provides:       crate(%{pkgname}/avx512) = %{version}
Provides:       crate(%{pkgname}/avx512-shaper-fixed-point-paths) = %{version}
Provides:       crate(%{pkgname}/avx512-shaper-optimized-paths) = %{version}
Provides:       crate(%{pkgname}/extended-range) = %{version}
Provides:       crate(%{pkgname}/in-place) = %{version}
Provides:       crate(%{pkgname}/lut) = %{version}
Provides:       crate(%{pkgname}/neon) = %{version}
Provides:       crate(%{pkgname}/neon-shaper-fixed-point-paths) = %{version}
Provides:       crate(%{pkgname}/neon-shaper-optimized-paths) = %{version}
Provides:       crate(%{pkgname}/neon-shaper-paths) = %{version}
Provides:       crate(%{pkgname}/options) = %{version}
Provides:       crate(%{pkgname}/sse) = %{version}
Provides:       crate(%{pkgname}/sse-shaper-fixed-point-paths) = %{version}
Provides:       crate(%{pkgname}/sse-shaper-optimized-paths) = %{version}
Provides:       crate(%{pkgname}/sse-shaper-paths) = %{version}

%description
Source code for takopackized Rust crate "moxcms"

%package     -n %{name}+avx-luts
Summary:        Simple Color Management in Rust - feature "avx_luts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/avx) = %{version}
Requires:       crate(%{pkgname}/lut) = %{version}
Provides:       crate(%{pkgname}/avx-luts) = %{version}

%description -n %{name}+avx-luts
This metapackage enables feature "avx_luts" for the Rust moxcms crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Simple Color Management in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/avx-luts) = %{version}
Requires:       crate(%{pkgname}/avx-shaper-fixed-point-paths) = %{version}
Requires:       crate(%{pkgname}/avx-shaper-paths) = %{version}
Requires:       crate(%{pkgname}/lut) = %{version}
Requires:       crate(%{pkgname}/neon-luts) = %{version}
Requires:       crate(%{pkgname}/neon-shaper-fixed-point-paths) = %{version}
Requires:       crate(%{pkgname}/neon-shaper-paths) = %{version}
Requires:       crate(%{pkgname}/sse-luts) = %{version}
Requires:       crate(%{pkgname}/sse-shaper-fixed-point-paths) = %{version}
Requires:       crate(%{pkgname}/sse-shaper-paths) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust moxcms crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+neon-luts
Summary:        Simple Color Management in Rust - feature "neon_luts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lut) = %{version}
Requires:       crate(%{pkgname}/neon) = %{version}
Provides:       crate(%{pkgname}/neon-luts) = %{version}

%description -n %{name}+neon-luts
This metapackage enables feature "neon_luts" for the Rust moxcms crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sse-luts
Summary:        Simple Color Management in Rust - feature "sse_luts"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/lut) = %{version}
Requires:       crate(%{pkgname}/sse) = %{version}
Provides:       crate(%{pkgname}/sse-luts) = %{version}

%description -n %{name}+sse-luts
This metapackage enables feature "sse_luts" for the Rust moxcms crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
