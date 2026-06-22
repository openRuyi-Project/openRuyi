# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tokio-vsock
%global full_version 0.7.2
%global pkgname tokio-vsock-0.7

Name:           rust-tokio-vsock-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "tokio-vsock"
License:        Apache-2.0
URL:            https://github.com/rust-vsock/tokio-vsock
#!RemoteAsset:  sha256:8b319ef9394889dab2e1b4f0085b45ba11d0c79dc9d1a9d1afc057d009d0f1c7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.3.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(libc-0.2/default) >= 0.2.172
Requires:       crate(tokio-1/default) >= 1.34.0
Requires:       crate(tokio-1/net) >= 1.34.0
Requires:       crate(tokio-1/sync) >= 1.34.0
Requires:       crate(vsock-0.5/default) >= 0.5.1
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "tokio-vsock"

%package     -n %{name}+axum08
Summary:        Asynchronous Virtio socket support for Rust - feature "axum08"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(axum-0.8/http1) >= 0.8.0
Requires:       crate(axum-0.8/tokio) >= 0.8.0
Provides:       crate(%{pkgname}/axum08) = %{version}

%description -n %{name}+axum08
This metapackage enables feature "axum08" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic010
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic010"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/tonic010) = %{version}

%description -n %{name}+tonic010
This metapackage enables feature "tonic010" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic011
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic011"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/tonic011) = %{version}

%description -n %{name}+tonic011
This metapackage enables feature "tonic011" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic012
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic012"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/tonic012) = %{version}

%description -n %{name}+tonic012
This metapackage enables feature "tonic012" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic013
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic013"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/tonic013) = %{version}

%description -n %{name}+tonic013
This metapackage enables feature "tonic013" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic014
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic014"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/tonic014) = %{version}

%description -n %{name}+tonic014
This metapackage enables feature "tonic014" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic05
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic05"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/tonic05) = %{version}

%description -n %{name}+tonic05
This metapackage enables feature "tonic05" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic06
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic06"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/tonic06) = %{version}

%description -n %{name}+tonic06
This metapackage enables feature "tonic06" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic07
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic07"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/tonic07) = %{version}

%description -n %{name}+tonic07
This metapackage enables feature "tonic07" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic08
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic08"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/tonic08) = %{version}

%description -n %{name}+tonic08
This metapackage enables feature "tonic08" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tonic09
Summary:        Asynchronous Virtio socket support for Rust - feature "tonic09"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/tonic09) = %{version}

%description -n %{name}+tonic09
This metapackage enables feature "tonic09" for the Rust tokio-vsock crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
