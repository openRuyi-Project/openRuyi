# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name piper
%global full_version 0.2.5
%global pkgname piper-0.2

Name:           rust-piper-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "piper"
License:        MIT OR Apache-2.0
URL:            https://github.com/smol-rs/piper
#!RemoteAsset:  sha256:c835479a4443ded371d6c535cbfd8d31ad92c5d23ae9770a61bc155e4992a3c1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(atomic-waker-1/default) >= 1.1.0
Requires:       crate(fastrand-2) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "piper"

%package     -n %{name}+futures-io
Summary:        Asynchronous single-consumer single-producer pipe for bytes - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.28
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust piper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Asynchronous single-consumer single-producer pipe for bytes - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/portable-atomic-crate) = %{version}
Requires:       crate(%{pkgname}/portable-atomic-util) = %{version}
Requires:       crate(atomic-waker-1/portable-atomic) >= 1.1.0
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust piper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-util
Summary:        Asynchronous single-consumer single-producer pipe for bytes - feature "portable-atomic-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.0
Requires:       crate(portable-atomic-util-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/portable-atomic-util) = %{version}

%description -n %{name}+portable-atomic-util
This metapackage enables feature "portable-atomic-util" for the Rust piper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic-crate
Summary:        Asynchronous single-consumer single-producer pipe for bytes - feature "portable_atomic_crate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-1) >= 1.2.0
Provides:       crate(%{pkgname}/portable-atomic-crate) = %{version}

%description -n %{name}+portable-atomic-crate
This metapackage enables feature "portable_atomic_crate" for the Rust piper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Asynchronous single-consumer single-producer pipe for bytes - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-io) = %{version}
Requires:       crate(fastrand-2/std) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust piper crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
