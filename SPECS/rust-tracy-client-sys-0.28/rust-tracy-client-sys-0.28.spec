# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracy-client-sys
%global full_version 0.28.0
%global pkgname tracy-client-sys-0.28

Name:           rust-tracy-client-sys-0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Rust crate "tracy-client-sys"
License:        (MIT OR Apache-2.0) AND BSD-3-Clause
URL:            https://github.com/nagisa/rust_tracy_client
#!RemoteAsset:  sha256:c5f7c95348f20c1c913d72157b3c6dee6ea3e30b3d19502c5a7f6d3f160dacbf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1) >= 1.0.83
Requires:       crate(windows-targets-0.48/default) >= 0.48.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/broadcast) = %{version}
Provides:       crate(%{pkgname}/callstack-inlines) = %{version}
Provides:       crate(%{pkgname}/code-transfer) = %{version}
Provides:       crate(%{pkgname}/context-switch-tracing) = %{version}
Provides:       crate(%{pkgname}/crash-handler) = %{version}
Provides:       crate(%{pkgname}/debuginfod) = %{version}
Provides:       crate(%{pkgname}/delayed-init) = %{version}
Provides:       crate(%{pkgname}/demangle) = %{version}
Provides:       crate(%{pkgname}/enable) = %{version}
Provides:       crate(%{pkgname}/fibers) = %{version}
Provides:       crate(%{pkgname}/flush-on-exit) = %{version}
Provides:       crate(%{pkgname}/manual-lifetime) = %{version}
Provides:       crate(%{pkgname}/ondemand) = %{version}
Provides:       crate(%{pkgname}/only-ipv4) = %{version}
Provides:       crate(%{pkgname}/only-localhost) = %{version}
Provides:       crate(%{pkgname}/sampling) = %{version}
Provides:       crate(%{pkgname}/system-tracing) = %{version}
Provides:       crate(%{pkgname}/timer-fallback) = %{version}
Provides:       crate(%{pkgname}/verify) = %{version}

%description
Source code for takopackized Rust crate "tracy-client-sys"

%package     -n %{name}+default
Summary:        Low level bindings to the client libraries for the Tracy profiler - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/broadcast) = %{version}
Requires:       crate(%{pkgname}/callstack-inlines) = %{version}
Requires:       crate(%{pkgname}/code-transfer) = %{version}
Requires:       crate(%{pkgname}/context-switch-tracing) = %{version}
Requires:       crate(%{pkgname}/crash-handler) = %{version}
Requires:       crate(%{pkgname}/enable) = %{version}
Requires:       crate(%{pkgname}/sampling) = %{version}
Requires:       crate(%{pkgname}/system-tracing) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracy-client-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
