# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tiny-skia
%global full_version 0.11.4
%global pkgname tiny-skia-0.11

Name:           rust-tiny-skia-0.11
Version:        0.11.4
Release:        %autorelease
Summary:        Rust crate "tiny-skia"
License:        BSD-3-Clause
URL:            https://github.com/RazrFalcon/tiny-skia
#!RemoteAsset:  sha256:83d13394d44dae3207b52a326c0c85a8bf87f1541f23b0d143811088497b09ab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayref-0.3/default) >= 0.3.6
Requires:       crate(arrayvec-0.7) >= 0.7.0
Requires:       crate(bytemuck-1/aarch64-simd) >= 1.12.0
Requires:       crate(bytemuck-1/default) >= 1.12.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(tiny-skia-path-0.11) >= 0.11.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}

%description
Source code for takopackized Rust crate "tiny-skia"

%package     -n %{name}+default
Summary:        Tiny Skia subset ported to Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/png-format) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tiny-skia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std-float
Summary:        Tiny Skia subset ported to Rust - feature "no-std-float"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tiny-skia-path-0.11/no-std-float) >= 0.11.4
Provides:       crate(%{pkgname}/no-std-float) = %{version}

%description -n %{name}+no-std-float
This metapackage enables feature "no-std-float" for the Rust tiny-skia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+png
Summary:        Tiny Skia subset ported to Rust - feature "png"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(png-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/png) = %{version}

%description -n %{name}+png
This metapackage enables feature "png" for the Rust tiny-skia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+png-format
Summary:        Tiny Skia subset ported to Rust - feature "png-format"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/png) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/png-format) = %{version}

%description -n %{name}+png-format
This metapackage enables feature "png-format" for the Rust tiny-skia crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Tiny Skia subset ported to Rust - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tiny-skia-path-0.11/std) >= 0.11.4
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tiny-skia crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
