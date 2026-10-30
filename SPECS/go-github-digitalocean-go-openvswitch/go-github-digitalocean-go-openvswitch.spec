# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-openvswitch
%define go_import_path  github.com/digitalocean/go-openvswitch
# kubecomps uses this fork through its go.mod replace directive.
%define commit_id       6b2d502be872efc533841c22be6f92da9ecd49b5

Name:           go-github-digitalocean-go-openvswitch
Version:        0+git20260922.6b2d502
Release:        %autorelease
Summary:        Go clients for Open vSwitch
License:        Apache-2.0
URL:            https://github.com/digitalocean/go-openvswitch
#!RemoteAsset:  sha256:c14b2845a9c179459d4f927d2c30ec48e8390ea69b1772801d7d093bc143dddf
Source0:        https://github.com/yousong/go-openvswitch/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Netlink flag compatibility from https://github.com/digitalocean/go-openvswitch/commit/bdadc6af1303873144e9c9c245b92ca56445c638
Patch1000:      1000-update-netlink-flags.patch

# The pinned fork uses numeric %%q formatting in RegMatch.GoString.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/mdlayher/genetlink)
BuildRequires:  go(github.com/mdlayher/netlink)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/mdlayher/genetlink)
Requires:       go(github.com/mdlayher/netlink)

%description
Go clients for Open vSwitch, the OVSDB protocol and the Linux Open vSwitch
generic netlink interface.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
