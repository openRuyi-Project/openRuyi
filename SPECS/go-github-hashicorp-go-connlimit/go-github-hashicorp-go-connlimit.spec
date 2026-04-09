# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-connlimit
%define go_import_path  github.com/hashicorp/go-connlimit

Name:           go-github-hashicorp-go-connlimit
Version:        0.3.1
Release:        %autorelease
Summary:        A simple library that allows a network server to limit how may concurrent connections it supports from each client IP.
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-connlimit
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-connlimit/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# openRuyi: stabilize a flaky HTTP concurrency test on newer Go/OBS environments
Patch0:         2000-tests-stabilize-TestHTTPServerWith429WithDuration.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/hashicorp/go-connlimit) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Go Server Client Connection Tracking

This package provides a library for network servers to track how many
concurrent connections they have from a given client address.

It's designed to be very simple and shared between several HashiCorp
products that provide network servers and need this kind of control to
impose limits on the resources that can be consumed by a single client.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
