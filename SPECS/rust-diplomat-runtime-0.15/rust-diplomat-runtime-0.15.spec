# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name diplomat-runtime
%global full_version 0.15.2
%global pkgname diplomat-runtime-0.15

Name:           rust-diplomat-runtime-0.15
Version:        0.15.2
Release:        %autorelease
Summary:        Rust crate "diplomat-runtime"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-diplomat/diplomat
#!RemoteAsset:  sha256:25b2f28ba90d2ffa95a531ea479769d4a6b2f5f187cd76ab5fd3bdcd64b3603e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "diplomat-runtime"

%package     -n %{name}+jvm-callback-support
Summary:        Common runtime utilities used by diplomat codegen - feature "jvm-callback-support"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jni-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/jvm-callback-support) = %{version}

%description -n %{name}+jvm-callback-support
This metapackage enables feature "jvm-callback-support" for the Rust diplomat-runtime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Common runtime utilities used by diplomat codegen - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust diplomat-runtime crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
