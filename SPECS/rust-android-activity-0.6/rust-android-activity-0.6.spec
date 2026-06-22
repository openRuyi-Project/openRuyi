# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name android-activity
%global full_version 0.6.1
%global pkgname android-activity-0.6

Name:           rust-android-activity-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "android-activity"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-mobile/android-activity
#!RemoteAsset:  sha256:0f2a1bb052857d5dd49572219344a7332b31b76405648eabac5bc68978251bcd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(android-properties-0.2/default) >= 0.2.0
Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(cc-1) >= 1.0.42
Requires:       crate(cc-1/parallel) >= 1.0.42
Requires:       crate(jni-0.22/default) >= 0.22.4
Requires:       crate(libc-0.2/default) >= 0.2.139
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(ndk-0.9) >= 0.9.0
Requires:       crate(ndk-context-0.1/default) >= 0.1.1
Requires:       crate(ndk-sys-0.6/default) >= 0.6.0
Requires:       crate(num-enum-0.7/default) >= 0.7.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/native-activity) = %{version}

%description
Source code for takopackized Rust crate "android-activity"

%package     -n %{name}+api-level-30
Summary:        Glue for building Rust applications on Android with NativeActivity or GameActivity - feature "api-level-30"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndk-0.9/api-level-30) >= 0.9.0
Provides:       crate(%{pkgname}/api-level-30) = %{version}

%description -n %{name}+api-level-30
This metapackage enables feature "api-level-30" for the Rust android-activity crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd-cesu8
Summary:        Glue for building Rust applications on Android with NativeActivity or GameActivity - feature "simd_cesu8" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(simd-cesu8-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/game-activity) = %{version}
Provides:       crate(%{pkgname}/simd-cesu8) = %{version}

%description -n %{name}+simd-cesu8
This metapackage enables feature "simd_cesu8" for the Rust android-activity crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "game-activity" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
