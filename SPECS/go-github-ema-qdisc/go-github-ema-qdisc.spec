# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           qdisc
%define go_import_path  github.com/ema/qdisc

Name:           go-github-ema-qdisc
Version:        1.0.0
Release:        %autorelease
Summary:        Go library for Linux queueing discipline information
License:        MIT
URL:            https://github.com/ema/qdisc
#!RemoteAsset:  sha256:5d32474cb5aa1d8a9b912a06afb485aab310450ca1bbb02e127ef7ba6b6260c7
Source0:        %{url}/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/mdlayher/netlink)

Provides:       go(github.com/ema/qdisc) = %{version}

Requires:       go(github.com/mdlayher/netlink)

%description
Go library for reading Linux traffic-control queueing disciplines over
netlink.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
