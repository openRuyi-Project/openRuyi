# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-packetline
%global full_version 0.19.3
%global pkgname gix-packetline-0.19

Name:           rust-gix-packetline-0.19
Version:        0.19.3
Release:        %autorelease
Summary:        Rust crate "gix-packetline"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:64286a8b5148e76ab80932e72762dd27ccf6169dd7a134b027c8a262a8262fcf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(faster-hex-0.10/std) >= 0.10.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/blocking-io)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "gix-packetline"

%package     -n %{name}+async-io
Summary:        The gitoxide project implementing the pkt-line serialization format - feature "async-io"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures-lite)
Requires:       crate(futures-io-0.3/default) >= 0.3.16
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname}/async-io)

%description -n %{name}+async-io
This metapackage enables feature "async-io" for the Rust gix-packetline crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        The gitoxide project implementing the pkt-line serialization format - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-packetline crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-lite
Summary:        The gitoxide project implementing the pkt-line serialization format - feature "futures-lite"
Requires:       crate(%{pkgname})
Requires:       crate(futures-lite-2.0/default) >= 2.1.0
Provides:       crate(%{pkgname}/futures-lite)

%description -n %{name}+futures-lite
This metapackage enables feature "futures-lite" for the Rust gix-packetline crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project implementing the pkt-line serialization format - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0/serde) >= 1.12.1
Requires:       crate(bstr-1.0/std) >= 1.12.1
Requires:       crate(faster-hex-0.10/serde) >= 0.10.0
Requires:       crate(faster-hex-0.10/std) >= 0.10.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Requires:       crate(serde-1.0/std) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-packetline crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
