# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name slice-ring-buffer
%global full_version 0.3.4
%global pkgname slice-ring-buffer-0.3

Name:           rust-slice-ring-buffer-0.3
Version:        0.3.4
Release:        %autorelease
Summary:        Rust crate "slice-ring-buffer"
License:        MIT OR Apache-2.0
URL:            https://github.com/liquidityc/slice_ring_buffer
#!RemoteAsset:  sha256:84ae312bda09b2368f79f985fdb4df4a0b5cbc75546b511303972d195f8c27d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2) >= 0.2.0
Requires:       crate(mach2-0.4) >= 0.4.1
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/memoryapi) >= 0.3.0
Requires:       crate(winapi-0.3/sysinfoapi) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/unix-sysv) = %{version}

%description
Source code for takopackized Rust crate "slice-ring-buffer"

%package     -n %{name}+use-std
Summary:        Double-ended queue that Deref's into a slice - feature "use_std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/use-std) >= 0.2.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/use-std) = %{version}

%description -n %{name}+use-std
This metapackage enables feature "use_std" for the Rust slice-ring-buffer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
