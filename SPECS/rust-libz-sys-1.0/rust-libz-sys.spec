# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libz-sys
%global full_version 1.1.25
%global pkgname libz-sys-1.0

Name:           rust-libz-sys-1.0
Version:        1.1.25
Release:        %autorelease
Summary:        Rust crate "libz-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/libz-sys
#!RemoteAsset:  sha256:d52f4c29e2a68ac30c9087e1b772dc9f44a2b66ed44edf2266cf2be9b03dafc1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.58
Requires:       crate(pkg-config-0.3/default) >= 0.3.32
Requires:       crate(vcpkg-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/asm)
Provides:       crate(%{pkgname}/static)
Provides:       crate(%{pkgname}/stock-zlib)

%description
Source code for takopackized Rust crate "libz-sys"

%package     -n %{name}+cmake
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "cmake"
Requires:       crate(%{pkgname})
Requires:       crate(cmake-0.1/default) >= 0.1.50
Provides:       crate(%{pkgname}/cmake)

%description -n %{name}+cmake
This metapackage enables feature "cmake" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/stock-zlib)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "libc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.184
Provides:       crate(%{pkgname}/libc)
Provides:       crate(%{pkgname}/zlib-ng-no-cmake-experimental-community-maintained)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zlib-ng-no-cmake-experimental-community-maintained" feature.

%package     -n %{name}+zlib-ng
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "zlib-ng"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cmake)
Requires:       crate(%{pkgname}/libc)
Provides:       crate(%{pkgname}/zlib-ng)

%description -n %{name}+zlib-ng
This metapackage enables feature "zlib-ng" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
