# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           dbus
%define go_import_path  github.com/godbus/dbus/v5
# Integration tests require a running D-Bus daemon.
%define go_test_ignore_failure 1

Name:           go-github-godbus-dbus
Version:        5.2.2
Release:        %autorelease
Summary:        Native Go bindings for D-Bus
License:        BSD-2-Clause
URL:            https://github.com/godbus/dbus
#!RemoteAsset:  sha256:f8d9e0df1350a834c169dc53ff75e5f630d0563802be51fbb60de283e2ea499c
Source0:        https://github.com/godbus/dbus/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
dbus is a simple library that implements native Go client bindings for
the D-Bus message bus system.

Features

 * Complete native implementation of the D-Bus message protocol
 * Go-like API (channels for signals / asynchronous method calls,
   Goroutine-safe connections)
 * Subpackages that help with the introspection / property interfaces

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
