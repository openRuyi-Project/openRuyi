# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-keystore
%global full_version 0.7.2
%global pkgname sequoia-keystore-0.7

Name:           rust-sequoia-keystore-0.7
Version:        0.7.2
Release:        %autorelease
Summary:        Rust crate "sequoia-keystore"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:50e5887d0c3c5f0df1d1cab937ef7a5c398111ddfd911c714f28c904438f229c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(async-generic-1/default) >= 1.1.0
Requires:       crate(capnp-0.25/default) >= 0.25.0
Requires:       crate(capnpc-0.25) >= 0.25.0
Requires:       crate(dirs-5/default) >= 5.0.0
Requires:       crate(env-logger-0.10/default) >= 0.10.0
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(paste-1/default) >= 1.0.0
Requires:       crate(sequoia-directories-0.1/default) >= 0.1.0
Requires:       crate(sequoia-ipc-0.36) >= 0.36.1
Requires:       crate(sequoia-keystore-backend-0.7/default) >= 0.7.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.21.0
Requires:       crate(tokio-1/io-std) >= 1.21.0
Requires:       crate(tokio-1/macros) >= 1.21.0
Requires:       crate(tokio-1/net) >= 1.21.0
Requires:       crate(tokio-1/rt) >= 1.21.0
Requires:       crate(tokio-util-0.7/compat) >= 0.7.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sequoia-keystore"

%package     -n %{name}+default
Summary:        Sequoia's private key store server - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gpg-agent) = %{version}
Requires:       crate(%{pkgname}/softkeys) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sequoia-keystore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gpg-agent
Summary:        Sequoia's private key store server - feature "gpg-agent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-keystore-gpg-agent-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/gpg-agent) = %{version}

%description -n %{name}+gpg-agent
This metapackage enables feature "gpg-agent" for the Rust sequoia-keystore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openpgp-card
Summary:        Sequoia's private key store server - feature "openpgp-card"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-keystore-openpgp-card-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/openpgp-card) = %{version}

%description -n %{name}+openpgp-card
This metapackage enables feature "openpgp-card" for the Rust sequoia-keystore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+softkeys
Summary:        Sequoia's private key store server - feature "softkeys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-keystore-softkeys-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/softkeys) = %{version}

%description -n %{name}+softkeys
This metapackage enables feature "softkeys" for the Rust sequoia-keystore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tpm
Summary:        Sequoia's private key store server - feature "tpm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-keystore-tpm-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/tpm) = %{version}

%description -n %{name}+tpm
This metapackage enables feature "tpm" for the Rust sequoia-keystore crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
