# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           paho.mqtt.golang
%define go_import_path  github.com/eclipse/paho.mqtt.golang
# Client tests expect a live MQTT broker.
%define go_test_ignore_failure 1

Name:           go-github-eclipse-paho.mqtt.golang
Version:        1.5.0
Release:        %autorelease
Summary:        Eclipse Paho MQTT 3.1/3.1.1 client for Go
License:        EPL-2.0 AND BSD-3-Clause
URL:            https://github.com/eclipse/paho.mqtt.golang
#!RemoteAsset:  sha256:7ccfa07cd9440900759678cb085e57b7d0dc665164602e5ecc64531296560366
Source0:        https://github.com/eclipse/paho.mqtt.golang/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)

Provides:       go(github.com/eclipse/paho.mqtt.golang) = %{version}

Requires:       go(github.com/gorilla/websocket)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)

%description
Eclipse Paho MQTT Go client implements MQTT 3.1/3.1.1, including
asynchronous publish and subscribe. MinIO uses it as an event
notification target.

%prep -a
# cmd holds sample programs and docker fixtures, not the library.
rm -rf cmd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
