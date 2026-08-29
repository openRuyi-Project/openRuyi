# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           globalping-cli
%define go_import_path  github.com/jsdelivr/globalping-cli

Name:           go-github-jsdelivr-globalping-cli
Version:        1.5.1
Release:        %autorelease
Summary:        Command-line client and Go library for Globalping
License:        MPL-2.0
URL:            https://github.com/jsdelivr/globalping-cli
VCS:            git:https://github.com/jsdelivr/globalping-cli.git
#!RemoteAsset:  sha256:235c96480e66b23c1393a5da56f1456908399207948300f1202b6fb335b71550
Source0:        https://github.com/jsdelivr/globalping-cli/archive/refs/tags/v%{version}.tar.gz#/globalping-cli-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n globalping-cli-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/andybalholm/brotli)
BuildRequires:  go(github.com/icza/backscanner)
BuildRequires:  go(github.com/mattn/go-runewidth)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/shirou/gopsutil)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
# testify is used by the selected library tests only.
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tklauser/go-sysconf)
BuildRequires:  go(go.uber.org/mock/gomock)
BuildRequires:  go(golang.org/x/term)

Provides:       go(github.com/jsdelivr/globalping-cli) = %{version}

Requires:       go(github.com/andybalholm/brotli)
Requires:       go(github.com/icza/backscanner)
Requires:       go(github.com/mattn/go-runewidth)
Requires:       go(github.com/pkg/errors)
Requires:       go(github.com/shirou/gopsutil)
Requires:       go(github.com/spf13/cobra)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/tklauser/go-sysconf)
Requires:       go(go.uber.org/mock/gomock)
Requires:       go(golang.org/x/term)

%description
Globalping CLI is a command-line client and reusable Go library for running
network measurements through the Globalping platform.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
