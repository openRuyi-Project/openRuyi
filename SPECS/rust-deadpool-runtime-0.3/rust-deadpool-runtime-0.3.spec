# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deadpool-runtime
%global full_version 0.3.1
%global pkgname deadpool-runtime-0.3

Name:           rust-deadpool-runtime-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "deadpool-runtime"
License:        MIT OR Apache-2.0
URL:            https://github.com/deadpool-rs/deadpool
#!RemoteAsset:  sha256:2657f61fb1dd8bf37a8d51093cc7cee4e77125b22f7753f49b289f831bec2bae
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "deadpool-runtime"

%package     -n %{name}+async-std-1
Summary:        Dead simple async pool utilities for async runtimes - feature "async-std_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.0.0
Requires:       crate(async-std-1/unstable) >= 1.0.0
Provides:       crate(%{pkgname}/async-std-1) = %{version}

%description -n %{name}+async-std-1
This metapackage enables feature "async-std_1" for the Rust deadpool-runtime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-2
Summary:        Dead simple async pool utilities for async runtimes - feature "smol_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-io-2/default) >= 2.0.0
Requires:       crate(blocking-1/default) >= 1.6.0
Requires:       crate(futures-lite-2/default) >= 2.6.0
Provides:       crate(%{pkgname}/smol-2) = %{version}

%description -n %{name}+smol-2
This metapackage enables feature "smol_2" for the Rust deadpool-runtime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-1
Summary:        Dead simple async pool utilities for async runtimes - feature "tokio_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Provides:       crate(%{pkgname}/tokio-1) = %{version}

%description -n %{name}+tokio-1
This metapackage enables feature "tokio_1" for the Rust deadpool-runtime crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
