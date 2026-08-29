# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hyper
%global full_version 1.9.0
%global pkgname hyper-1

Name:           rust-hyper-1
Version:        1.9.0
Release:        %autorelease
Summary:        Rust crate "hyper"
License:        MIT
URL:            https://hyper.rs
#!RemoteAsset:  sha256:6299f016b246a94207e63da54dbe807655bf9e00044f73ded42c3ac5305fbcca
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.2.0
Requires:       crate(http-1/default) >= 1.0.0
Requires:       crate(http-body-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/capi) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/nightly) = %{version}

%description
Source code for takopackized Rust crate "hyper"

%package     -n %{name}+client
Summary:        Protective and efficient HTTP library for all - feature "client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.4
Requires:       crate(smallvec-1/const-generics) >= 1.12.0
Requires:       crate(smallvec-1/const-new) >= 1.12.0
Requires:       crate(smallvec-1/default) >= 1.12.0
Requires:       crate(want-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/client) = %{version}

%description -n %{name}+client
This metapackage enables feature "client" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffi
Summary:        Protective and efficient HTTP library for all - feature "ffi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3/alloc) >= 0.3.0
Requires:       crate(http-body-util-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/ffi) = %{version}

%description -n %{name}+ffi
This metapackage enables feature "ffi" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Protective and efficient HTTP library for all - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/client) = %{version}
Requires:       crate(%{pkgname}/http1) = %{version}
Requires:       crate(%{pkgname}/http2) = %{version}
Requires:       crate(%{pkgname}/server) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http1
Summary:        Protective and efficient HTTP library for all - feature "http1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(atomic-waker-1/default) >= 1.1.2
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-core-0.3/default) >= 0.3.31
Requires:       crate(httparse-1/default) >= 1.9.0
Requires:       crate(itoa-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/http1) = %{version}

%description -n %{name}+http1
This metapackage enables feature "http1" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http2
Summary:        Protective and efficient HTTP library for all - feature "http2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-core-0.3/default) >= 0.3.31
Requires:       crate(h2-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/http2) = %{version}

%description -n %{name}+http2
This metapackage enables feature "http2" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+server
Summary:        Protective and efficient HTTP library for all - feature "server"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(httpdate-1/default) >= 1.0.0
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.4
Requires:       crate(smallvec-1/const-generics) >= 1.12.0
Requires:       crate(smallvec-1/const-new) >= 1.12.0
Requires:       crate(smallvec-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/server) = %{version}

%description -n %{name}+server
This metapackage enables feature "server" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Protective and efficient HTTP library for all - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust hyper crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
