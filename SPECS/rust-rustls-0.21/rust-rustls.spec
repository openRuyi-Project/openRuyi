# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls
%global full_version 0.21.12
%global pkgname rustls-0.21

Name:           rust-rustls-0.21
Version:        0.21.12
Release:        %autorelease
Summary:        Rust crate "rustls"
License:        Apache-2.0 OR ISC OR MIT
URL:            https://github.com/rustls/rustls
#!RemoteAsset:  sha256:3f56a14d1f48b391359b22f731fd4bd7e43c97f3c50eee276f3aa09c94784d3e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ring-0.17/default) >= 0.17.0
Requires:       crate(rustls-webpki-0.101/alloc) >= 0.101.7
Requires:       crate(rustls-webpki-0.101/default) >= 0.101.7
Requires:       crate(rustls-webpki-0.101/std) >= 0.101.7
Requires:       crate(sct-0.7/default) >= 0.7.0
Provides:       crate(rustls) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/dangerous-configuration)
Provides:       crate(%{pkgname}/quic)
Provides:       crate(%{pkgname}/secret-extraction)
Provides:       crate(%{pkgname}/tls12)

%description
Source code for takopackized Rust crate "rustls"

%package     -n %{name}+default
Summary:        Modern TLS library written in Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/logging)
Requires:       crate(%{pkgname}/tls12)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Modern TLS library written in Rust - feature "log" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%package     -n %{name}+rustversion
Summary:        Modern TLS library written in Rust - feature "rustversion" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustversion-1.0/default) >= 1.0.6
Provides:       crate(%{pkgname}/read-buf)
Provides:       crate(%{pkgname}/rustversion)

%description -n %{name}+rustversion
This metapackage enables feature "rustversion" for the Rust rustls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "read_buf" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
