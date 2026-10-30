# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           paho.golang
%define go_import_path  github.com/eclipse/paho.golang

Name:           go-github-eclipse-paho.golang
Version:        0.23.0
Release:        %autorelease
Summary:        Eclipse Paho MQTT 5 client for Go
License:        EPL-2.0 OR BSD-3-Clause
URL:            https://github.com/eclipse/paho.golang
#!RemoteAsset:  sha256:52e0635272aa6eb29a59778f7131d6a24ed41008569e11297f7a5bf742cd38aa
Source0:        https://github.com/eclipse/paho.golang/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/eclipse-paho/paho.golang/pull/347
Patch2000:      2000-fix-file-queue-store-order-on-coarse-mtime.patch
# Synchronize quota assertions independently of builder scheduling latency.
Patch2001:      2001-synchronize-send-quota-test.patch

# The quota regression test uses testing/synctest.
BuildRequires:  go >= 1.25
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/goleak)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(gopkg.in/yaml.v3)

# The module root is a virtual capability; its client lives in paho.
Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/autopaho) = %{version}
Provides:       go(%{go_import_path}/autopaho/extensions/rpc) = %{version}
Provides:       go(%{go_import_path}/autopaho/queue) = %{version}
Provides:       go(%{go_import_path}/autopaho/queue/file) = %{version}
Provides:       go(%{go_import_path}/autopaho/queue/memory) = %{version}
Provides:       go(%{go_import_path}/internal/basictestserver) = %{version}
Provides:       go(%{go_import_path}/internal/testserver) = %{version}
Provides:       go(%{go_import_path}/packets) = %{version}
Provides:       go(%{go_import_path}/paho) = %{version}
Provides:       go(%{go_import_path}/paho/extensions/rpc) = %{version}
Provides:       go(%{go_import_path}/paho/extensions/topicaliases) = %{version}
Provides:       go(%{go_import_path}/paho/log) = %{version}
Provides:       go(%{go_import_path}/paho/session) = %{version}
Provides:       go(%{go_import_path}/paho/session/state) = %{version}
Provides:       go(%{go_import_path}/paho/store/file) = %{version}
Provides:       go(%{go_import_path}/paho/store/memory) = %{version}

Requires:       go(github.com/gorilla/websocket)
Requires:       go(golang.org/x/net)

%description
Eclipse Paho provides an MQTT 5 client, packet encoding, session stores,
and the autopaho connection and reconnection manager. The complete
repository includes examples, extensions, and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
