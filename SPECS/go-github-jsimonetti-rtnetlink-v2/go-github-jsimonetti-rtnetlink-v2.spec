# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rtnetlink
%define go_import_path  github.com/jsimonetti/rtnetlink/v2
# Root tests import cilium/ebpf, whose link tests import rtnetlink/v2.
%define go_test_exclude  %{go_import_path}

Name:           go-github-jsimonetti-rtnetlink-v2
Version:        2.2.0
Release:        %autorelease
Summary:        Low-level Linux rtnetlink library for Go
License:        MIT
URL:            https://github.com/jsimonetti/rtnetlink
#!RemoteAsset:  sha256:fab1f59db068c705f1dc8dbb9120180dd7710a1c950c23ff0cf6ee6052d2c582
Source0:        https://github.com/jsimonetti/rtnetlink/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(github.com/mdlayher/socket)
BuildRequires:  go(golang.org/x/exp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/mdlayher/netlink)
Requires:       go(github.com/mdlayher/socket)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
Rtnetlink provides low-level access to Linux routing netlink messages from Go.

%check -a
# Root tests are excluded to break the cilium/ebpf test dependency cycle, so
# compile the root package explicitly to retain a basic source check.
GO111MODULE=off GOPATH=%{_builddir}/go:%{_datadir}/gocode \
    go build %{go_import_path}

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
