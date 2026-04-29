# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-protocol
%global full_version 0.51.0
%global pkgname gix-protocol-0.51

Name:           rust-gix-protocol-0.51
Version:        0.51.0
Release:        %autorelease
Summary:        Rust crate "gix-protocol"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:12b4b807c47ffcf7c1e5b8119585368a56449f3493da93b931e1d4239364e922
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(gix-date-0.10/default) >= 0.10.7
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-ref-0.53/default) >= 0.53.1
Requires:       crate(gix-shallow-0.5/default) >= 0.5.0
Requires:       crate(gix-transport-0.48/default) >= 0.48.0
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(maybe-async-0.2/default) >= 0.2.10
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(winnow-0.7/default) >= 0.7.15
Requires:       crate(winnow-0.7/simd) >= 0.7.15
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-protocol"

%package     -n %{name}+async-client
Summary:        The gitoxide project for implementing git protocols - feature "async-client"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fetch)
Requires:       crate(%{pkgname}/futures-lite)
Requires:       crate(%{pkgname}/handshake)
Requires:       crate(async-trait-0.1/default) >= 0.1.51
Requires:       crate(futures-io-0.3/default) >= 0.3.16
Requires:       crate(gix-transport-0.48/async-client) >= 0.48.0
Provides:       crate(%{pkgname}/async-client)

%description -n %{name}+async-client
This metapackage enables feature "async-client" for the Rust gix-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-client
Summary:        The gitoxide project for implementing git protocols - feature "blocking-client"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fetch)
Requires:       crate(%{pkgname}/handshake)
Requires:       crate(gix-transport-0.48/blocking-client) >= 0.48.0
Requires:       crate(maybe-async-0.2/is-sync) >= 0.2.10
Provides:       crate(%{pkgname}/blocking-client)

%description -n %{name}+blocking-client
This metapackage enables feature "blocking-client" for the Rust gix-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        The gitoxide project for implementing git protocols - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fetch
Summary:        The gitoxide project for implementing git protocols - feature "fetch"
Requires:       crate(%{pkgname})
Requires:       crate(gix-lock-18.0/default) >= 18.0.0
Requires:       crate(gix-negotiate-0.21/default) >= 0.21.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-refspec-0.31/default) >= 0.31.0
Requires:       crate(gix-revwalk-0.21/default) >= 0.21.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Provides:       crate(%{pkgname}/fetch)

%description -n %{name}+fetch
This metapackage enables feature "fetch" for the Rust gix-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-lite
Summary:        The gitoxide project for implementing git protocols - feature "futures-lite"
Requires:       crate(%{pkgname})
Requires:       crate(futures-lite-2.0/default) >= 2.1.0
Provides:       crate(%{pkgname}/futures-lite)

%description -n %{name}+futures-lite
This metapackage enables feature "futures-lite" for the Rust gix-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+handshake
Summary:        The gitoxide project for implementing git protocols - feature "handshake"
Requires:       crate(%{pkgname})
Requires:       crate(gix-credentials-0.30/default) >= 0.30.0
Provides:       crate(%{pkgname}/handshake)

%description -n %{name}+handshake
This metapackage enables feature "handshake" for the Rust gix-protocol crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project for implementing git protocols - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/serde) >= 1.12.1
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(bstr-1.0/unicode) >= 1.12.1
Requires:       crate(gix-hash-0.19/serde) >= 0.19.0
Requires:       crate(gix-shallow-0.5/serde) >= 0.5.0
Requires:       crate(gix-transport-0.48/serde) >= 0.48.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-protocol crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
