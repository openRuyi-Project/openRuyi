# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name buffer-redux
%global full_version 1.1.0
%global pkgname buffer-redux-1

Name:           rust-buffer-redux-1
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "buffer-redux"
License:        MIT OR Apache-2.0
URL:            https://github.com/dignifiedquire/buffer-redux
#!RemoteAsset:  sha256:431a9cc8d7efa49bc326729264537f5e60affce816c66edf434350778c9f4f54
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2/default) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "buffer-redux"

%package     -n %{name}+slice-deque
Summary:        Drop-in replacements for buffered I/O in `std::io` with extra features - feature "slice-deque" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slice-ring-buffer-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/slice-deque) = %{version}

%description -n %{name}+slice-deque
This metapackage enables feature "slice-deque" for the Rust buffer-redux crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
