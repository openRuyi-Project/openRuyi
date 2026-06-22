# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jni
%global full_version 0.22.4
%global pkgname jni-0.22

Name:           rust-jni-0.22
Version:        0.22.4
Release:        %autorelease
Summary:        Rust crate "jni"
License:        MIT OR Apache-2.0
URL:            https://github.com/jni-rs/jni-rs
#!RemoteAsset:  sha256:5efd9a482cf3a427f00d6b35f14332adc7902ce91efb778580e180ff90fa3498
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(combine-4/default) >= 4.1.0
Requires:       crate(jni-macros-0.22/default) >= 0.22.4
Requires:       crate(jni-sys-0.4/default) >= 0.4.1
Requires:       crate(log-0.4/default) >= 0.4.4
Requires:       crate(simd-cesu8-1/default) >= 1.1.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(walkdir-2) >= 2.0.0
Requires:       crate(windows-link-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/cfg-test) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "jni"

%package     -n %{name}+invocation
Summary:        Rust bindings to the JNI - feature "invocation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(java-locator-0.1/default) >= 0.1.3
Requires:       crate(libloading-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/invocation) = %{version}

%description -n %{name}+invocation
This metapackage enables feature "invocation" for the Rust jni crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
