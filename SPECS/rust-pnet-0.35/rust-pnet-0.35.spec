# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pnet
%global full_version 0.35.0
%global pkgname pnet-0.35

Name:           rust-pnet-0.35
Version:        0.35.0
Release:        %autorelease
Summary:        Rust crate "pnet"
License:        MIT OR Apache-2.0
URL:            https://github.com/libpnet/libpnet
#!RemoteAsset:  sha256:682396b533413cc2e009fbb48aadf93619a149d3e57defba19ff50ce0201bd0d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pnet-base-0.35) >= 0.35.0
Requires:       crate(pnet-packet-0.35) >= 0.35.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/appveyor) = %{version}
Provides:       crate(%{pkgname}/benchmark) = %{version}
Provides:       crate(%{pkgname}/travis) = %{version}

%description
Source code for takopackized Rust crate "pnet"

%package     -n %{name}+ipnetwork
Summary:        Cross-platform, low level networking using the Rust programming language - feature "ipnetwork"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ipnetwork-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/ipnetwork) = %{version}

%description -n %{name}+ipnetwork
This metapackage enables feature "ipnetwork" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+netmap
Summary:        Cross-platform, low level networking using the Rust programming language - feature "netmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-datalink-0.35/netmap) >= 0.35.0
Requires:       crate(pnet-datalink-0.35/netmap-sys) >= 0.35.0
Provides:       crate(%{pkgname}/netmap) = %{version}

%description -n %{name}+netmap
This metapackage enables feature "netmap" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pcap
Summary:        Cross-platform, low level networking using the Rust programming language - feature "pcap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-datalink-0.35/pcap) >= 0.35.0
Provides:       crate(%{pkgname}/pcap) = %{version}

%description -n %{name}+pcap
This metapackage enables feature "pcap" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pnet-datalink
Summary:        Cross-platform, low level networking using the Rust programming language - feature "pnet_datalink"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-datalink-0.35) >= 0.35.0
Provides:       crate(%{pkgname}/pnet-datalink) = %{version}

%description -n %{name}+pnet-datalink
This metapackage enables feature "pnet_datalink" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pnet-sys
Summary:        Cross-platform, low level networking using the Rust programming language - feature "pnet_sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-sys-0.35) >= 0.35.0
Provides:       crate(%{pkgname}/pnet-sys) = %{version}

%description -n %{name}+pnet-sys
This metapackage enables feature "pnet_sys" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pnet-transport
Summary:        Cross-platform, low level networking using the Rust programming language - feature "pnet_transport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-transport-0.35) >= 0.35.0
Provides:       crate(%{pkgname}/pnet-transport) = %{version}

%description -n %{name}+pnet-transport
This metapackage enables feature "pnet_transport" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Cross-platform, low level networking using the Rust programming language - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pnet-base-0.35/serde) >= 0.35.0
Requires:       crate(pnet-datalink-0.35/serde) >= 0.35.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Cross-platform, low level networking using the Rust programming language - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ipnetwork) = %{version}
Requires:       crate(%{pkgname}/pnet-datalink) = %{version}
Requires:       crate(%{pkgname}/pnet-sys) = %{version}
Requires:       crate(%{pkgname}/pnet-transport) = %{version}
Requires:       crate(pnet-base-0.35/std) >= 0.35.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pnet crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
