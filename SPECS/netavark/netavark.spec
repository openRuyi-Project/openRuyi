# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           netavark
Version:        1.17.1
Release:        %autorelease
License:        Apache-2.0 AND BSD-3-Clause AND MIT
Summary:        OCI network stack
URL:            https://github.com/containers/netavark
#!RemoteAsset
Source0:        https://github.com/containers/netavark/archive/v%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/containers/netavark/releases/download/v%{version}/netavark-v%{version}-vendor.tar.gz
# TODO: pseudo build system, for ease of use
# will be replaced by build system cargo
BuildSystem:    autotools

BuildOption(build):  NETAVARK_DEFAULT_FW=nftables
BuildOption(build):  CARGO="cargo --offline"
BuildOption(build):  CI=1
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  make
BuildRequires:  go-md2man
# needs protoc binary, not protobuf library
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  systemd
BuildRequires:  pkgconfig(systemd)

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

%prep -a
tar xzf %{SOURCE1}
cat << EOF > .cargo/config.toml
[target.'cfg(linux)']
runner = 'unshare -rn'

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%conf
# there's no configure

%build -a
# may need to contain dependencies' license
cd docs
%__make

%check
# there's no check

%preun
%systemd_preun netavark-dhcp-proxy.service netavark-firewalld-reload.service netavark-nftables-reload.service

%postun
%systemd_postun netavark-dhcp-proxy.service netavark-firewalld-reload.service netavark-nftables-reload.service

%files
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/netavark*
%{_mandir}/man1/netavark.1*
%{_mandir}/man7/netavark-firewalld.7*
%{_unitdir}/netavark-dhcp-proxy.service
%{_unitdir}/netavark-dhcp-proxy.socket
%{_unitdir}/netavark-firewalld-reload.service
%{_unitdir}/netavark-nftables-reload.service

%changelog
%autochangelog
