# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name smoltcp
%global full_version 0.13.1
%global pkgname smoltcp-0.13

Name:           rust-smoltcp-0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Rust crate "smoltcp"
License:        0BSD
URL:            https://github.com/smoltcp-rs/smoltcp
#!RemoteAsset:  sha256:5f73d40463bba65efc9adc6370b56df76d563cc46e2482bba58351b4afb7535e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1) >= 1.0.0
Requires:       crate(byteorder-1) >= 1.0.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(heapless-0.9/default) >= 0.9.0
Requires:       crate(managed-0.8/map) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/assembler-max-segment-count-1) = %{version}
Provides:       crate(%{pkgname}/assembler-max-segment-count-16) = %{version}
Provides:       crate(%{pkgname}/assembler-max-segment-count-2) = %{version}
Provides:       crate(%{pkgname}/assembler-max-segment-count-3) = %{version}
Provides:       crate(%{pkgname}/assembler-max-segment-count-32) = %{version}
Provides:       crate(%{pkgname}/assembler-max-segment-count-4) = %{version}
Provides:       crate(%{pkgname}/assembler-max-segment-count-8) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/auto-icmp-echo-reply) = %{version}
Provides:       crate(%{pkgname}/dns-max-name-size-128) = %{version}
Provides:       crate(%{pkgname}/dns-max-name-size-255) = %{version}
Provides:       crate(%{pkgname}/dns-max-name-size-64) = %{version}
Provides:       crate(%{pkgname}/dns-max-result-count-1) = %{version}
Provides:       crate(%{pkgname}/dns-max-result-count-16) = %{version}
Provides:       crate(%{pkgname}/dns-max-result-count-2) = %{version}
Provides:       crate(%{pkgname}/dns-max-result-count-3) = %{version}
Provides:       crate(%{pkgname}/dns-max-result-count-32) = %{version}
Provides:       crate(%{pkgname}/dns-max-result-count-4) = %{version}
Provides:       crate(%{pkgname}/dns-max-result-count-8) = %{version}
Provides:       crate(%{pkgname}/dns-max-server-count-1) = %{version}
Provides:       crate(%{pkgname}/dns-max-server-count-16) = %{version}
Provides:       crate(%{pkgname}/dns-max-server-count-2) = %{version}
Provides:       crate(%{pkgname}/dns-max-server-count-3) = %{version}
Provides:       crate(%{pkgname}/dns-max-server-count-32) = %{version}
Provides:       crate(%{pkgname}/dns-max-server-count-4) = %{version}
Provides:       crate(%{pkgname}/dns-max-server-count-8) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-1024) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-1500) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-16384) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-2048) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-256) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-32768) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-4096) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-512) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-65536) = %{version}
Provides:       crate(%{pkgname}/fragmentation-buffer-size-8192) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-1) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-2) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-3) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-4) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-5) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-6) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-7) = %{version}
Provides:       crate(%{pkgname}/iface-max-addr-count-8) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-1) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-1024) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-128) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-16) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-2) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-256) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-3) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-32) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-4) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-5) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-512) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-6) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-64) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-7) = %{version}
Provides:       crate(%{pkgname}/iface-max-multicast-group-count-8) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-1) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-2) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-3) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-4) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-5) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-6) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-7) = %{version}
Provides:       crate(%{pkgname}/iface-max-prefix-count-8) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-0) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-1) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-1024) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-128) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-16) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-2) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-256) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-3) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-32) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-4) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-5) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-512) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-6) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-64) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-7) = %{version}
Provides:       crate(%{pkgname}/iface-max-route-count-8) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-1) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-1024) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-128) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-16) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-2) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-256) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-3) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-32) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-4) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-5) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-512) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-6) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-64) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-7) = %{version}
Provides:       crate(%{pkgname}/iface-max-sixlowpan-address-context-count-8) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-1) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-1024) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-128) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-16) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-2) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-256) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-3) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-32) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-4) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-5) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-512) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-6) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-64) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-7) = %{version}
Provides:       crate(%{pkgname}/iface-neighbor-cache-count-8) = %{version}
Provides:       crate(%{pkgname}/ipv6-hbh-max-options-1) = %{version}
Provides:       crate(%{pkgname}/ipv6-hbh-max-options-16) = %{version}
Provides:       crate(%{pkgname}/ipv6-hbh-max-options-2) = %{version}
Provides:       crate(%{pkgname}/ipv6-hbh-max-options-3) = %{version}
Provides:       crate(%{pkgname}/ipv6-hbh-max-options-32) = %{version}
Provides:       crate(%{pkgname}/ipv6-hbh-max-options-4) = %{version}
Provides:       crate(%{pkgname}/ipv6-hbh-max-options-8) = %{version}
Provides:       crate(%{pkgname}/medium-ethernet) = %{version}
Provides:       crate(%{pkgname}/medium-ip) = %{version}
Provides:       crate(%{pkgname}/multicast) = %{version}
Provides:       crate(%{pkgname}/netsim) = %{version}
Provides:       crate(%{pkgname}/packetmeta-id) = %{version}
Provides:       crate(%{pkgname}/proto-dhcpv4) = %{version}
Provides:       crate(%{pkgname}/proto-dns) = %{version}
Provides:       crate(%{pkgname}/proto-fragmentation) = %{version}
Provides:       crate(%{pkgname}/proto-ipsec-ah) = %{version}
Provides:       crate(%{pkgname}/proto-ipsec-esp) = %{version}
Provides:       crate(%{pkgname}/proto-ipv4) = %{version}
Provides:       crate(%{pkgname}/proto-ipv6) = %{version}
Provides:       crate(%{pkgname}/proto-ipv6-hbh) = %{version}
Provides:       crate(%{pkgname}/proto-ipv6-routing) = %{version}
Provides:       crate(%{pkgname}/proto-ipv6-slaac) = %{version}
Provides:       crate(%{pkgname}/proto-sixlowpan) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-count-1) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-count-16) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-count-2) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-count-3) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-count-32) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-count-4) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-count-8) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-1024) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-1500) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-16384) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-2048) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-256) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-32768) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-4096) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-512) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-65536) = %{version}
Provides:       crate(%{pkgname}/reassembly-buffer-size-8192) = %{version}
Provides:       crate(%{pkgname}/rpl-parents-buffer-count-16) = %{version}
Provides:       crate(%{pkgname}/rpl-parents-buffer-count-2) = %{version}
Provides:       crate(%{pkgname}/rpl-parents-buffer-count-32) = %{version}
Provides:       crate(%{pkgname}/rpl-parents-buffer-count-4) = %{version}
Provides:       crate(%{pkgname}/rpl-parents-buffer-count-8) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-1) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-128) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-16) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-2) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-32) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-4) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-64) = %{version}
Provides:       crate(%{pkgname}/rpl-relations-buffer-count-8) = %{version}
Provides:       crate(%{pkgname}/socket) = %{version}
Provides:       crate(%{pkgname}/socket-icmp) = %{version}
Provides:       crate(%{pkgname}/socket-raw) = %{version}
Provides:       crate(%{pkgname}/socket-tcp) = %{version}
Provides:       crate(%{pkgname}/socket-tcp-cubic) = %{version}
Provides:       crate(%{pkgname}/socket-tcp-pause-synack) = %{version}
Provides:       crate(%{pkgname}/socket-tcp-reno) = %{version}
Provides:       crate(%{pkgname}/socket-udp) = %{version}
Provides:       crate(%{pkgname}/verbose) = %{version}

%description
Source code for the Rust crate "smoltcp"

%package     -n %{name}+alloc
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.3/alloc) >= 0.3.8
Requires:       crate(defmt-0.3/ip-in-core) >= 0.3.8
Requires:       crate(managed-0.8/alloc) >= 0.8.0
Requires:       crate(managed-0.8/map) >= 0.8.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/auto-icmp-echo-reply) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/medium-ethernet) = %{version}
Requires:       crate(%{pkgname}/medium-ieee802154) = %{version}
Requires:       crate(%{pkgname}/medium-ip) = %{version}
Requires:       crate(%{pkgname}/multicast) = %{version}
Requires:       crate(%{pkgname}/packetmeta-id) = %{version}
Requires:       crate(%{pkgname}/phy-raw-socket) = %{version}
Requires:       crate(%{pkgname}/phy-tuntap-interface) = %{version}
Requires:       crate(%{pkgname}/proto-dhcpv4) = %{version}
Requires:       crate(%{pkgname}/proto-dns) = %{version}
Requires:       crate(%{pkgname}/proto-ipv4) = %{version}
Requires:       crate(%{pkgname}/proto-ipv4-fragmentation) = %{version}
Requires:       crate(%{pkgname}/proto-ipv6) = %{version}
Requires:       crate(%{pkgname}/proto-ipv6-slaac) = %{version}
Requires:       crate(%{pkgname}/proto-sixlowpan-fragmentation) = %{version}
Requires:       crate(%{pkgname}/socket-dhcpv4) = %{version}
Requires:       crate(%{pkgname}/socket-dns) = %{version}
Requires:       crate(%{pkgname}/socket-icmp) = %{version}
Requires:       crate(%{pkgname}/socket-mdns) = %{version}
Requires:       crate(%{pkgname}/socket-raw) = %{version}
Requires:       crate(%{pkgname}/socket-tcp) = %{version}
Requires:       crate(%{pkgname}/socket-udp) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+defmt
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "defmt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(defmt-0.3/default) >= 0.3.8
Requires:       crate(defmt-0.3/ip-in-core) >= 0.3.8
Requires:       crate(heapless-0.9/defmt) >= 0.9.0
Provides:       crate(%{pkgname}/defmt) = %{version}

%description -n %{name}+defmt
This metapackage enables feature "defmt" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.18
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.4
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+medium-ieee802154
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "medium-ieee802154"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proto-sixlowpan) = %{version}
Requires:       crate(%{pkgname}/socket) = %{version}
Provides:       crate(%{pkgname}/medium-ieee802154) = %{version}

%description -n %{name}+medium-ieee802154
This metapackage enables feature "medium-ieee802154" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phy-raw-socket
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "phy-raw_socket" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/phy-raw-socket) = %{version}
Provides:       crate(%{pkgname}/phy-tuntap-interface) = %{version}

%description -n %{name}+phy-raw-socket
This metapackage enables feature "phy-raw_socket" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "phy-tuntap_interface" feature.

%package     -n %{name}+proto-ipsec
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "proto-ipsec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proto-ipsec-ah) = %{version}
Requires:       crate(%{pkgname}/proto-ipsec-esp) = %{version}
Provides:       crate(%{pkgname}/proto-ipsec) = %{version}

%description -n %{name}+proto-ipsec
This metapackage enables feature "proto-ipsec" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proto-ipv4-fragmentation
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "proto-ipv4-fragmentation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proto-fragmentation) = %{version}
Requires:       crate(%{pkgname}/proto-ipv4) = %{version}
Provides:       crate(%{pkgname}/proto-ipv4-fragmentation) = %{version}

%description -n %{name}+proto-ipv4-fragmentation
This metapackage enables feature "proto-ipv4-fragmentation" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proto-ipv6-fragmentation
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "proto-ipv6-fragmentation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proto-fragmentation) = %{version}
Requires:       crate(%{pkgname}/proto-ipv6) = %{version}
Provides:       crate(%{pkgname}/proto-ipv6-fragmentation) = %{version}

%description -n %{name}+proto-ipv6-fragmentation
This metapackage enables feature "proto-ipv6-fragmentation" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proto-rpl
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "proto-rpl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proto-ipv6-hbh) = %{version}
Requires:       crate(%{pkgname}/proto-ipv6-routing) = %{version}
Provides:       crate(%{pkgname}/proto-rpl) = %{version}

%description -n %{name}+proto-rpl
This metapackage enables feature "proto-rpl" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proto-sixlowpan-fragmentation
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "proto-sixlowpan-fragmentation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proto-fragmentation) = %{version}
Requires:       crate(%{pkgname}/proto-sixlowpan) = %{version}
Provides:       crate(%{pkgname}/proto-sixlowpan-fragmentation) = %{version}

%description -n %{name}+proto-sixlowpan-fragmentation
This metapackage enables feature "proto-sixlowpan-fragmentation" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket-dhcpv4
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "socket-dhcpv4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/medium-ethernet) = %{version}
Requires:       crate(%{pkgname}/proto-dhcpv4) = %{version}
Requires:       crate(%{pkgname}/socket) = %{version}
Provides:       crate(%{pkgname}/socket-dhcpv4) = %{version}

%description -n %{name}+socket-dhcpv4
This metapackage enables feature "socket-dhcpv4" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+socket-dns
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "socket-dns" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/proto-dns) = %{version}
Requires:       crate(%{pkgname}/socket) = %{version}
Provides:       crate(%{pkgname}/socket-dns) = %{version}
Provides:       crate(%{pkgname}/socket-mdns) = %{version}

%description -n %{name}+socket-dns
This metapackage enables feature "socket-dns" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "socket-mdns" feature.

%package     -n %{name}+std
Summary:        TCP/IP stack designed for bare-metal, real-time systems without a heap - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(managed-0.8/map) >= 0.8.0
Requires:       crate(managed-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust smoltcp crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE-0BSD.txt
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
