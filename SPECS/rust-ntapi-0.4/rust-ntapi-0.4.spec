# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ntapi
%global full_version 0.4.3
%global pkgname ntapi-0.4

Name:           rust-ntapi-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "ntapi"
License:        Apache-2.0 OR MIT
URL:            https://github.com/MSxDOS/ntapi
#!RemoteAsset:  sha256:c3b335231dfd352ffb0f8017f3b6027a4917f7df785ea2143d8af2adc66980ae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winapi-0.3/cfg) >= 0.3.9
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/evntrace) >= 0.3.9
Requires:       crate(winapi-0.3/in6addr) >= 0.3.9
Requires:       crate(winapi-0.3/inaddr) >= 0.3.9
Requires:       crate(winapi-0.3/minwinbase) >= 0.3.9
Requires:       crate(winapi-0.3/ntsecapi) >= 0.3.9
Requires:       crate(winapi-0.3/windef) >= 0.3.9
Requires:       crate(winapi-0.3/winioctl) >= 0.3.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/func-types) = %{version}
Provides:       crate(%{pkgname}/kernel) = %{version}
Provides:       crate(%{pkgname}/user) = %{version}

%description
Source code for takopackized Rust crate "ntapi"

%package     -n %{name}+impl-default
Summary:        FFI bindings for Native API - feature "impl-default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(winapi-0.3/cfg) >= 0.3.9
Requires:       crate(winapi-0.3/evntrace) >= 0.3.9
Requires:       crate(winapi-0.3/impl-default) >= 0.3.9
Requires:       crate(winapi-0.3/in6addr) >= 0.3.9
Requires:       crate(winapi-0.3/inaddr) >= 0.3.9
Requires:       crate(winapi-0.3/minwinbase) >= 0.3.9
Requires:       crate(winapi-0.3/ntsecapi) >= 0.3.9
Requires:       crate(winapi-0.3/windef) >= 0.3.9
Requires:       crate(winapi-0.3/winioctl) >= 0.3.9
Provides:       crate(%{pkgname}/impl-default) = %{version}

%description -n %{name}+impl-default
This metapackage enables feature "impl-default" for the Rust ntapi crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
