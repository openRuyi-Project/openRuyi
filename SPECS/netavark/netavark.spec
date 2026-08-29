# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           netavark
Version:        1.17.1
Release:        %autorelease
License:        Apache-2.0 AND BSD-3-Clause AND MIT
Summary:        OCI network stack
URL:            https://github.com/containers/netavark
#!RemoteAsset:  sha256:22cdaea57490014c8faf029d0e2d585d9fddcfcb35fc342f812ba79b27d5d3d1
Source0:        https://github.com/containers/netavark/archive/v%{version}.tar.gz
BuildSystem:    rust

# Relax the clap requirement to allow compatible 4.x providers.
Patch2000:      2000-fix-version.patch

BuildOption(build):  -- --bin netavark --bin netavark-dhcp-proxy-client --bin netavark-connection-tester

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  make
BuildRequires:  go-md2man
# build.rs needs a protoc binary for generated DHCP proxy bindings.
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  systemd
BuildRequires:  pkgconfig(systemd)

BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(chrono-0.4/clock) >= 0.4.44
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(clap-4/env) >= 4.6.1
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.10
BuildRequires:  crate(fs2-0.4/default) >= 0.4.3
BuildRequires:  crate(futures-channel-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-core-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-util-0.3/default) >= 0.3.32
BuildRequires:  crate(hyper-util-0.1/default) >= 0.1.20
BuildRequires:  crate(ipnet-2/default) >= 2.12.0
BuildRequires:  crate(ipnet-2/serde) >= 2.12.0
BuildRequires:  crate(iptables-0.6/default) >= 0.6.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(log-0.4/default) >= 0.4.30
BuildRequires:  crate(mozim-0.3/default) >= 0.3.1
BuildRequires:  crate(netlink-packet-core-0.8/default) >= 0.8.1
BuildRequires:  crate(netlink-packet-route-0.25/default) >= 0.25.1
BuildRequires:  crate(netlink-sys-0.8/default) >= 0.8.7
BuildRequires:  crate(nftables-0.6/default) >= 0.6.3
BuildRequires:  crate(nix-0.30/default) >= 0.30.1
BuildRequires:  crate(nix-0.30/net) >= 0.30.1
BuildRequires:  crate(nix-0.30/sched) >= 0.30.1
BuildRequires:  crate(nix-0.30/signal) >= 0.30.1
BuildRequires:  crate(nix-0.30/socket) >= 0.30.1
BuildRequires:  crate(nix-0.30/user) >= 0.30.1
BuildRequires:  crate(once-cell-1/default) >= 1.21.4
BuildRequires:  crate(prost-0.14/default) >= 0.14.1
BuildRequires:  crate(rand-0.9/default) >= 0.9.4
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(sha2-0.10/default) >= 0.10.9
BuildRequires:  crate(tempfile-3/default) >= 3.27.0
BuildRequires:  crate(tokio-1/default) >= 1.52.3
BuildRequires:  crate(tokio-1/fs) >= 1.52.3
BuildRequires:  crate(tokio-1/rt) >= 1.52.3
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.52.3
BuildRequires:  crate(tokio-1/signal) >= 1.52.3
BuildRequires:  crate(tokio-1/time) >= 1.52.3
BuildRequires:  crate(tokio-stream-0.1/default) >= 0.1.18
BuildRequires:  crate(tokio-stream-0.1/net) >= 0.1.18
BuildRequires:  crate(tonic-0.14/default) >= 0.14.2
BuildRequires:  crate(tonic-prost-0.14/default) >= 0.14.2
BuildRequires:  crate(tonic-prost-build-0.14/default) >= 0.14.2
BuildRequires:  crate(tower-0.5/default) >= 0.5.3
BuildRequires:  crate(tower-0.5/util) >= 0.5.3
BuildRequires:  crate(zbus-5/default) >= 5.15.0

Requires:       nftables
Requires:       aardvark-dns

%description
%{summary}

Netavark is a rust based network stack for containers. It is being
designed to work with Podman but is also applicable for other OCI
container management applications.

Netavark is a tool for configuring networking for Linux containers.
Its features include:
* Configuration of container networks via JSON configuration file
* Creation and management of required network interfaces,
    including MACVLAN networks
* All required firewall configuration to perform NAT and port
    forwarding as required for containers
* Support for iptables, firewalld and nftables
* Support for rootless containers
* Support for IPv4 and IPv6
* Support for container DNS resolution via aardvark-dns.

%build -p
%ifarch riscv64
export RUST_MIN_STACK=16777216
export CARGO_PROFILE_RELEASE_OPT_LEVEL=2
%endif
export NETAVARK_DEFAULT_FW=nftables
%__make -C docs

%install
mkdir -p bin
install -Dm0755 target/release/netavark bin/netavark
install -Dm0755 target/release/netavark-dhcp-proxy-client bin/netavark-dhcp-proxy-client
install -Dm0755 target/release/netavark-connection-tester bin/netavark-connection-tester

%__make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBEXECDIR=%{_libexecdir} \
  LIBEXECPODMAN=%{_libexecdir}/podman SYSTEMDDIR=%{_unitdir} install

%check
# Upstream's tests require network namespace setup, bats, and a
# container-oriented environment. Keep the build check minimal here.

%preun
%systemd_preun netavark-dhcp-proxy.service netavark-firewalld-reload.service netavark-nftables-reload.service

%postun
%systemd_postun netavark-dhcp-proxy.service netavark-firewalld-reload.service netavark-nftables-reload.service

%files
%doc README.md
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/netavark
%{_mandir}/man1/netavark.1*
%{_mandir}/man7/netavark-firewalld.7*
%{_unitdir}/netavark-dhcp-proxy.service
%{_unitdir}/netavark-dhcp-proxy.socket
%{_unitdir}/netavark-firewalld-reload.service
%{_unitdir}/netavark-nftables-reload.service

%changelog
%autochangelog
