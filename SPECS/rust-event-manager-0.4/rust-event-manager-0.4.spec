# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name event-manager
%global full_version 0.4.2
%global pkgname event-manager-0.4

Name:           rust-event-manager-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "event-manager"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/event-manager
#!RemoteAsset:  sha256:13bdac971eb2efaceffca0976058ab80c715945cc565c8a4aa1ed3bb0dc8d0e4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(vmm-sys-util-0.12/default) >= 0.12.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "event-manager"

%package     -n %{name}+remote-endpoint
Summary:        Event manager abstractions - feature "remote_endpoint"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/remote-endpoint) = %{version}

%description -n %{name}+remote-endpoint
This metapackage enables feature "remote_endpoint" for the Rust event-manager crate.

%package     -n %{name}+test-utilities
Summary:        Event manager abstractions - feature "test_utilities"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/test-utilities) = %{version}

%description -n %{name}+test-utilities
This metapackage enables feature "test_utilities" for the Rust event-manager crate.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
