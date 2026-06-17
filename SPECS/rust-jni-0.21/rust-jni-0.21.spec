# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jni
%global full_version 0.21.1
%global pkgname jni-0.21

Name:           rust-jni-0.21
Version:        0.21.1
Release:        %autorelease
Summary:        Rust crate "jni"
License:        MIT OR Apache-2.0
URL:            https://github.com/jni-rs/jni-rs
#!RemoteAsset:  sha256:1a87aa2bb7d2af34197c04845522473242e1aa17c12f4935d5856491a7fb8c97
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cesu8-1/default) >= 1.1.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(combine-4/default) >= 4.1.0
Requires:       crate(jni-sys-0.3/default) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.4
Requires:       crate(thiserror-1/default) >= 1.0.20
Requires:       crate(walkdir-2) >= 2.0.0
Requires:       crate(windows-sys-0.45/default) >= 0.45.0
Requires:       crate(windows-sys-0.45/win32-globalization) >= 0.45.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "jni"

%package     -n %{name}+invocation
Summary:        Rust bindings to the JNI - feature "invocation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/java-locator) = %{version}
Requires:       crate(%{pkgname}/libloading) = %{version}
Provides:       crate(%{pkgname}/invocation) = %{version}

%description -n %{name}+invocation
This metapackage enables feature "invocation" for the Rust jni crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+java-locator
Summary:        Rust bindings to the JNI - feature "java-locator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(java-locator-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/java-locator) = %{version}

%description -n %{name}+java-locator
This metapackage enables feature "java-locator" for the Rust jni crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libloading
Summary:        Rust bindings to the JNI - feature "libloading"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libloading-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/libloading) = %{version}

%description -n %{name}+libloading
This metapackage enables feature "libloading" for the Rust jni crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
