# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name embedded-io
%global full_version 0.4.0
%global pkgname embedded-io-0.4

Name:           rust-embedded-io-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "embedded-io"
License:        MIT OR Apache-2.0
URL:            https://github.com/embassy-rs/embedded-io
#!RemoteAsset:  sha256:ef1a6892d9eef45c8fa6b9e0086428a2cca8491aca8f787c534a3d6d0bcb3ced
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "embedded-io"

%package     -n %{name}+defmt
Summary:        Embedded IO traits - feature "defmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/defmt) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust embedded-io crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Embedded IO traits - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(futures-0.3) >= 0.3.21
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust embedded-io crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Embedded IO traits - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.14
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust embedded-io crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Embedded IO traits - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(futures-0.3/std) >= 0.3.21
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust embedded-io crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Embedded IO traits - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(tokio-1/net) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust embedded-io crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
