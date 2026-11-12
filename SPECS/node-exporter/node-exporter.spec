# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           node_exporter
%define go_import_path  github.com/prometheus/node_exporter

Name:           node-exporter
Version:        1.12.1
Release:        %autorelease
Summary:        Prometheus exporter for host hardware and operating system metrics
License:        Apache-2.0
URL:            https://github.com/prometheus/node_exporter
#!RemoteAsset:  sha256:a90f1df0fde58d216d4a7d342e64831d2e3257db8084deadbe69754d34b15142
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source1:        node-exporter.service
Source2:        node-exporter.sysusers
Source3:        node-exporter.sysconfig
BuildSystem:    golang
BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go >= 1.25
BuildRequires:  go-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/beevik/ntp)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/dennwc/btrfs)
BuildRequires:  go(github.com/ema/qdisc)
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/hashicorp/go-envparse)
BuildRequires:  go(github.com/hodgesds/perf-utils)
BuildRequires:  go(github.com/jsimonetti/rtnetlink/v2)
BuildRequires:  go(github.com/mattn/go-xmlrpc)
BuildRequires:  go(github.com/mdlayher/ethtool)
BuildRequires:  go(github.com/mdlayher/genetlink)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(github.com/mdlayher/wifi)
BuildRequires:  go(github.com/opencontainers/selinux)
BuildRequires:  go(github.com/prometheus-community/go-runit)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/exporter-toolkit)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/safchain/ethtool)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(howett.net/plist)

%{?systemd_requires}

%description
Node Exporter exposes host hardware and operating system metrics in the
Prometheus text format. It includes collectors for CPU, memory, filesystem,
network, and other Linux subsystems.

%build
%go_common
CGO_ENABLED=0 %{__go} build %{go_build_flags_default} \
    -ldflags "-X github.com/prometheus/common/version.Version=%{version}" \
    -o %{_builddir}/node_exporter .

%install
install -Dpm0755 %{_builddir}/node_exporter %{buildroot}%{_bindir}/node_exporter
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/node-exporter.service
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/node-exporter.conf
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/node-exporter

%check
%{buildroot}%{_bindir}/node_exporter --version

%pre
%sysusers_create_package %{name} %{SOURCE2}

%post
%systemd_post node-exporter.service

%preun
%systemd_preun node-exporter.service

%postun
%systemd_postun_with_restart node-exporter.service

%files
%doc README.md CHANGELOG.md
%license LICENSE NOTICE
%{_bindir}/node_exporter
%{_unitdir}/node-exporter.service
%{_sysusersdir}/node-exporter.conf
%config(noreplace) %{_sysconfdir}/sysconfig/node-exporter

%changelog
%autochangelog
