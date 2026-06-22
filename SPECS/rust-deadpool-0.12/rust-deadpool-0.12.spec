# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name deadpool
%global full_version 0.12.3
%global pkgname deadpool-0.12

Name:           rust-deadpool-0.12
Version:        0.12.3
Release:        %autorelease
Summary:        Rust crate "deadpool"
License:        MIT OR Apache-2.0
URL:            https://github.com/bikeshedder/deadpool
#!RemoteAsset:  sha256:0be2b1d1d6ec8d846f05e137292d0b89133caf95ef33695424c09568bdd39b1b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(deadpool-runtime-0.1/default) >= 0.1.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(num-cpus-1/default) >= 1.11.1
Requires:       crate(tokio-1/default) >= 1.5.0
Requires:       crate(tokio-1/sync) >= 1.5.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/managed) = %{version}
Provides:       crate(%{pkgname}/unmanaged) = %{version}

%description
Source code for takopackized Rust crate "deadpool"

%package     -n %{name}+default
Summary:        Dead simple async pool - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/managed) = %{version}
Requires:       crate(%{pkgname}/unmanaged) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-async-std-1
Summary:        Dead simple async pool - feature "rt_async-std_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(deadpool-runtime-0.1/async-std-1) >= 0.1.0
Provides:       crate(%{pkgname}/rt-async-std-1) = %{version}

%description -n %{name}+rt-async-std-1
This metapackage enables feature "rt_async-std_1" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rt-tokio-1
Summary:        Dead simple async pool - feature "rt_tokio_1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(deadpool-runtime-0.1/tokio-1) >= 0.1.0
Provides:       crate(%{pkgname}/rt-tokio-1) = %{version}

%description -n %{name}+rt-tokio-1
This metapackage enables feature "rt_tokio_1" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Dead simple async pool - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.103
Requires:       crate(serde-1/derive) >= 1.0.103
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust deadpool crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
