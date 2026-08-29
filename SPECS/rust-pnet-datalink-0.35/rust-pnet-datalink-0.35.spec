# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pnet_datalink
%global full_version 0.35.0
%global pkgname pnet-datalink-0.35

Name:           rust-pnet-datalink-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "pnet_datalink"
License:        MIT OR Apache-2.0
URL:            https://github.com/libpnet/libpnet
#!RemoteAsset:  sha256:e79e70ec0be163102a332e1d2d5586d362ad76b01cec86f830241f2b6452a7b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ipnetwork-0.20/default) >= 0.20.0
Requires:       crate(libc-0.2/default) >= 0.2.147
Requires:       crate(pnet-base-0.35) >= 0.35.0
Requires:       crate(pnet-sys-0.35/default) >= 0.35.0
Requires:       crate(winapi-0.3/default) >= 0.3.9
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/netmap) = %{version}

%description
Source code for takopackized Rust crate "pnet_datalink"

%package     -n %{name}+netmap-sys
Summary:        Cross-platform, datalink layer networking - feature "netmap_sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(netmap-sys-0.1/default) >= 0.1.4
Requires:       crate(netmap-sys-0.1/netmap-with-libs) >= 0.1.4
Provides:       crate(%{pkgname}/netmap-sys) = %{version}

%description -n %{name}+netmap-sys
This metapackage enables feature "netmap_sys" for the Rust pnet_datalink crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pcap
Summary:        Cross-platform, datalink layer networking - feature "pcap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pcap-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/pcap) = %{version}

%description -n %{name}+pcap
This metapackage enables feature "pcap" for the Rust pnet_datalink crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Cross-platform, datalink layer networking - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.171
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pnet_datalink crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Cross-platform, datalink layer networking - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-base-0.35/std) >= 0.35.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pnet_datalink crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
