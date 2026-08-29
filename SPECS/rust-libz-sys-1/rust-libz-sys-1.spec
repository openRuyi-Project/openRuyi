# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libz-sys
%global full_version 1.1.28
%global pkgname libz-sys-1

Name:           rust-libz-sys-1
Version:        1.1.28
Release:        %autorelease
Summary:        Rust crate "libz-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/libz-sys
#!RemoteAsset:  sha256:fc3a226e576f50782b3305c5ccf458698f92798987f551c6a02efe8276721e22
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.98
Requires:       crate(pkg-config-0.3) >= 0.3.9
Requires:       crate(vcpkg-0.2) >= 0.2.11
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/asm) = %{version}
Provides:       crate(%{pkgname}/static) = %{version}
Provides:       crate(%{pkgname}/stock-zlib) = %{version}

%description
Source code for takopackized Rust crate "libz-sys"

%package     -n %{name}+cmake
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "cmake"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cmake-0.1/default) >= 0.1.50
Provides:       crate(%{pkgname}/cmake) = %{version}

%description -n %{name}+cmake
This metapackage enables feature "cmake" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/stock-zlib) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "libc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.43
Provides:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/zlib-ng-no-cmake-experimental-community-maintained) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zlib-ng-no-cmake-experimental-community-maintained" feature.

%package     -n %{name}+zlib-ng
Summary:        Low-level bindings to the system libz library (also known as zlib) - feature "zlib-ng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cmake) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Provides:       crate(%{pkgname}/zlib-ng) = %{version}

%description -n %{name}+zlib-ng
This metapackage enables feature "zlib-ng" for the Rust libz-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
