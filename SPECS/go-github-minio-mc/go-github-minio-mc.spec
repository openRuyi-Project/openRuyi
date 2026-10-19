# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           mc
%global go_import_path  github.com/minio/mc
%global commit_id cf909e1063a9a0aea7926378b0c416ed0eea7742

Name:           go-github-minio-mc
Version:        2025.03.12T17.29.24Z+git20261020.cf909e1
Release:        %autorelease
Summary:        MinIO client Go libraries
License:        AGPL-3.0-or-later
URL:            https://github.com/minio/mc
#!RemoteAsset:  sha256:aff96a5eb9694dfefe21c9bc090021b0ae33df68b960429b07abe3cd5adc89ea
Source0:        https://github.com/minio/mc/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go printf analysis rejects the eight non-constant format calls in this snapshot.
Patch2000:      2000-use-constant-formats-for-console-output.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/charmbracelet/bubbles)
BuildRequires:  go(github.com/charmbracelet/bubbles/viewport)
BuildRequires:  go(github.com/charmbracelet/bubbletea)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/cheggaaa/pb)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/golang-jwt/jwt/v4)
BuildRequires:  go(github.com/google/shlex)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/jedib0t/go-pretty/v6)
BuildRequires:  go(github.com/juju/ratelimit)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/mattn/go-ieproxy)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/minio/cli)
BuildRequires:  go(github.com/minio/colorjson)
BuildRequires:  go(github.com/minio/filepath)
BuildRequires:  go(github.com/minio/madmin-go/v3)
BuildRequires:  go(github.com/minio/minio-go/v7)
BuildRequires:  go(github.com/minio/pkg/v3)
BuildRequires:  go(github.com/minio/selfupdate)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/muesli/reflow)
BuildRequires:  go(github.com/muesli/termenv)
# OBS has both incompatible tablewriter APIs under the same import path.
# This mc snapshot uses the v0.0.5 API pinned in its upstream go.mod.
BuildRequires:  go(github.com/olekukonko/tablewriter) = 0.0.5
BuildRequires:  go(github.com/pkg/xattr)
BuildRequires:  go(github.com/posener/complete)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/rjeczalik/notify)
BuildRequires:  go(github.com/rs/xid)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/vbauerster/mpb/v8)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/check.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/minio/mc) = %{version}

Requires:       go(github.com/charmbracelet/bubbles)
Requires:       go(github.com/charmbracelet/bubbles/viewport)
Requires:       go(github.com/charmbracelet/bubbletea)
Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/cheggaaa/pb)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/fatih/color)
Requires:       go(github.com/golang-jwt/jwt/v4)
Requires:       go(github.com/google/shlex)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/inconshreveable/mousetrap)
Requires:       go(github.com/jedib0t/go-pretty/v6)
Requires:       go(github.com/juju/ratelimit)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/mattn/go-ieproxy)
Requires:       go(github.com/mattn/go-isatty)
Requires:       go(github.com/minio/cli)
Requires:       go(github.com/minio/colorjson)
Requires:       go(github.com/minio/filepath)
Requires:       go(github.com/minio/madmin-go/v3)
Requires:       go(github.com/minio/minio-go/v7)
Requires:       go(github.com/minio/pkg/v3)
Requires:       go(github.com/minio/selfupdate)
Requires:       go(github.com/mitchellh/go-homedir)
Requires:       go(github.com/muesli/reflow)
Requires:       go(github.com/muesli/termenv)
Requires:       go(github.com/olekukonko/tablewriter) = 0.0.5
Requires:       go(github.com/pkg/xattr)
Requires:       go(github.com/posener/complete)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/procfs)
Requires:       go(github.com/rjeczalik/notify)
Requires:       go(github.com/rs/xid)
Requires:       go(github.com/shirou/gopsutil/v3)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/vbauerster/mpb/v8)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/yaml.v2)

%description
Go libraries from the MinIO client, including its command handlers and
error reporting helpers, used by the MinIO Console.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
