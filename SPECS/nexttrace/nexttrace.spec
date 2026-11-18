# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Go -trimpath removes filesystem source paths, leaving no files for an
# automatically generated debugsource subpackage.
%undefine _debugsource_packages

%define _name           nexttrace
%define go_import_path  github.com/nxtrace/NTrace-core

Name:           nexttrace
Version:        1.7.6
Release:        %autorelease
Summary:        Full-featured visual route tracing tool
License:        GPL-3.0-only
URL:            https://github.com/nxtrace/NTrace-core
VCS:            git:https://github.com/nxtrace/NTrace-core.git
#!RemoteAsset:  sha256:4956737ace65a2ae7623e291287c258493016f481fae96699c693f3c3fdd5e27
Source0:        https://github.com/nxtrace/NTrace-core/archive/refs/tags/v%{version}.tar.gz#/NTrace-core-%{version}.tar.gz
BuildSystem:    golang

# Avoid embedding and shipping Windows-only prebuilt DLL/SYS files on Linux.
Patch2000:      2000-disable-windivert-on-non-windows.patch

# Inject fixed release metadata because upstream defaults are placeholders; a fixed date also keeps builds reproducible.
BuildOption(build):  -ldflags "-X github.com/nxtrace/NTrace-core/config.Version=v%{version} -X github.com/nxtrace/NTrace-core/config.BuildDate=2026-11-06T16:04:32Z -X github.com/nxtrace/NTrace-core/config.CommitID=c93eabd"

BuildRequires:  go >= 1.27.3
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/akamensky/argparse)
BuildRequires:  go(github.com/ameshkov/dnscrypt/v2)
BuildRequires:  go(github.com/charmbracelet/log)
BuildRequires:  go(github.com/charmbracelet/x/ansi)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/google/gopacket)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/jedisct1/go-dnsstamps)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/jsdelivr/globalping-cli)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/modelcontextprotocol/go-sdk)
BuildRequires:  go(github.com/natesales/q)
BuildRequires:  go(github.com/oschwald/maxminddb-golang)
BuildRequires:  go(github.com/quic-go/quic-go)
BuildRequires:  go(github.com/rodaine/table)
BuildRequires:  go(github.com/spf13/viper)
BuildRequires:  go(github.com/sthorne/odoh-go)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/syndtr/gocapability)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tsosunchia/powclient)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)

%description
NextTrace is an open-source network tracing tool that provides fast route analysis, IP/ASN information, and latency diagnostics with a user-friendly interface.

%prep
%autosetup -p1 -n NTrace-core-%{version}
rm -rf assets/windivert/x64 assets/windivert/x86

%go_prep

%check
%go_common
cd %{_builddir}/go/src/%{go_import_path}
go test . ./cmd ./config ./dn42 ./fast_trace ./internal/... ./ipgeo ./pow ./printer ./reporter ./server ./trace/... ./tracelog ./tracemap ./util ./wshandle

%files
%doc README.md README_zh_CN.md
%license LICENSE
%attr(0755,root,root) %caps(cap_net_raw,cap_net_admin=ep) %{_bindir}/nexttrace

%changelog
%autochangelog
